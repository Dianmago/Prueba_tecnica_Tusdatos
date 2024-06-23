import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from bs4 import BeautifulSoup
import csv

def consultar_causas(documento):
    opts = Options()
    opts.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36")

    chromedriver_path = 'C:\\chromedriver-win64\\chromedriver.exe'

    service = Service(chromedriver_path)

    driver = webdriver.Chrome(service=service, options=opts)

    driver.get('https://procesosjudiciales.funcionjudicial.gob.ec/busqueda-filtros')

    try:
        input_id = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, './/input[@formcontrolname="cedulaDemandado"]'))
        )

        input_id.clear()
        input_id.send_keys(documento)

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@type="submit" and @aria-label="Enviar formulario"]'))
        )

        login_button.click()
        sleep(random.uniform(2, 2.5))

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//strong[text()="Cédula/RUC/Pasaporte del Demandado/Procesado:"]'))
        )

        # Extraer la cédula del demandante consultado
        demandados = driver.find_elements(By.XPATH, '//strong[text()="Cédula/RUC/Pasaporte del Demandado/Procesado:"]/following-sibling::span')
        for demandado in demandados:
            cedula = demandado.text.strip()
            print(f'Cédula/RUC/Pasaporte del Demandado/Procesado: {cedula}')

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        causas = soup.select('div.cuerpo > div.causa-individual')

        with open('procesos_judicialesDemandado.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Escribir encabezados si el archivo está vacío
            if file.tell() == 0:
                writer.writerow(['Cédula/RUC/Pasaporte del Demandado/Procesado', 'No', 'Fecha de ingreso', 'No. proceso', 'Acción/Infracción', 'Detalle',
                                 'Número de incidente', 'Fecha de movimiento', 'Actores/Ofendidos',
                                 'Demandados/Procesados', 'Actuaciones Judiciales'])

            for causa in causas:
                numero = causa.find('div', class_='id').text.strip()
                fecha = causa.find('div', class_='fecha').text.strip()
                numero_proceso = causa.find('div', class_='numero-proceso').text.strip()
                accion_infraccion = causa.find('div', class_='accion-infraccion').text.strip()
                detalle = causa.find('div', class_='detalle').find('a')['href']

                detalle_link = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, f'//a[@href="/movimientos" and contains(@aria-label, "{numero_proceso}")]'))
                )
                detalle_link.click()

                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//section[@class="lista-movimientos"]'))
                )
                sleep(3)

                detalle_html = driver.page_source
                detalle_soup = BeautifulSoup(detalle_html, 'html.parser')

                movimientos = detalle_soup.select('div.lista-movimiento-individual')
                for movimiento in movimientos:
                    numero_incidente = movimiento.find('div', class_='numero-incidente').text.strip()
                    fecha_movimiento = movimiento.find('div', class_='fecha-ingreso').text.strip()
                    actores = movimiento.find('div', class_='lista-actores').text.strip()
                    demandados = movimiento.find('div', class_='lista-demandados').text.strip()
                    actuaciones_judiciales = movimiento.find('div', class_='actuaciones-judiciales').find('a')['aria-label']

                    writer.writerow([cedula, numero, fecha, numero_proceso, accion_infraccion, detalle,
                                     numero_incidente, fecha_movimiento, actores, demandados, actuaciones_judiciales])

                back_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Botón regresar"]'))
                )
                back_button.click()

                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//strong[text()="Cédula/RUC/Pasaporte del Demandado/Procesado:"]'))
                )
                sleep(random.uniform(1, 1.5))

            file.close()

        driver.get('https://procesosjudiciales.funcionjudicial.gob.ec/causas')

        # Verificar si hay más páginas disponibles
        next_button_xpath = '//button[@aria-label="Página siguiente"]'
        while True:
            try:
                next_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, next_button_xpath))
                )
                next_button.click()
                sleep(random.uniform(2, 2.5))
            except:
                print("No hay más páginas disponibles.")
                break

            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            causas = soup.select('div.cuerpo > div.causa-individual')

            with open('procesos_judicialesDemandado.csv', mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)

                for causa in causas:
                    numero = causa.find('div', class_='id').text.strip()
                    fecha = causa.find('div', class_='fecha').text.strip()
                    numero_proceso = causa.find('div', class_='numero-proceso').text.strip()
                    accion_infraccion = causa.find('div', class_='accion-infraccion').text.strip()
                    detalle = causa.find('div', class_='detalle').find('a')['href']

                    writer.writerow([cedula, numero, fecha, numero_proceso, accion_infraccion, detalle, '', '', '', '', ''])

            file.close()

    finally:
        driver.quit()

# Lista de cédulas a consultar
ids = ['1791251237001', '0968599020001']

# Procesar cada cédula
for documento in ids:
    print(f"Consultando información para cédula: {documento}")
    consultar_causas(documento)
