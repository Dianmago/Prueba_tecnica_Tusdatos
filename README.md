# Prueba Desarrollador Jr. de soporte técnico

## Punto 1:
Especificación: Lenguaje de programación: Python.

Se requiere extraer información de la página web "[Consulta de Procesos Judiciales](https://procesosjudiciales.funcionjudicial.gob.ec/busqueda-filtros)" 

utilizando técnicas de Web Scraping. La información se debe limpiar y guardar de 
manera estructurada. 

La página permite realizar búsquedas para Personas Naturales o Personas Jurídicas, 
utilizando criterios como Actor/Ofendido o Demandado/Procesado. Además, es preciso 
proporcionar documentos de identidad para Personas Naturales y RUC para Personas 
Jurídicas. Se adjunta una lista de datos de prueba para facilitar el proceso de extracción 
de información:

Tabla de CC:

| **Actor/Ofendido** | **Demandado/Procesado** |
|----------------|---------------------|
| 0968599020001  | 1791251237001       |
| 0992339411001  | 0968599020001       |

Teniendo en cuenta los datos de la tabla el scraping debe tener las siguientes características:

* Extraer listado de procesos que genera la búsqueda.
* Distinguir entre los procesos de demandado y demandante. 
* Extraer el detalle para cada proceso.
* Extraer todas las actuaciones judiciales de cada proceso.
* Guardar toda la información de los procesos en base de datos o un archivo (csv, json, etc).
* Crear y documentar un caso de prueba dentro del cual se ejecuten 15 consultas paralelas revisando que no haya un bloqueo por parte de la página de consulta.
* Implementación de tests

Nota: 
Considerando la potencial cantidad de procesos y subprocesos involucrados, es fundamental identificar el método más eficiente para la extracción de datos.

Implementación.

**Pasos:**

**Instalación de librerías:**

Como primer punto, es necesario instalar las librerías de Python requeridas en el código, para esto con “pip” podemos instalar directamente desde la consola:

"pip install random2 selenium beautifulsoup4"

El módulo random está incluido en la biblioteca estándar de Python, por lo que no necesitas instalarlo. Sin embargo, otros módulos como selenium y beautifulsoup4 sí necesitan ser instalados.

Una vez instaladas las librerías, es necesario, en nuestro caso y para poder ejecutar nuestro código, **instalar el Web Driver de Chrome.**

El WebDriver es una herramienta utilizada para automatizar navegadores web. Se usa comúnmente en pruebas automatizadas, scraping de datos y otras tareas que requieren la simulación de la interacción de un usuario con un navegador web. 

En nuestro código lo utilizamos para acceder a la página de "Consulta de Procesos Judiciales" y hacer el proceso de Web Scraping automatizado.

Los pasos para instalar son: 

1.	Descargar el WebDriver: 

    •	Ve al sitio web oficial de ChromeDriver: 'https://developer.chrome.com/docs/chromedriver/downloads?hl=es-419'
    •	Descarga la versión del WebDriver que coincida con la versión de tu navegador Chrome y el sistema operativo que estás usando.

2.	Configurar el WebDriver:

    •	Una vez descargado el archivo chromedriver.exe, colócalo en un directorio de tu elección y asegúrate de anotar la ruta completa del archivo.
    En nuestro caso está en : 
    'C:\\chromedriver-win64\\chromedriver.exe'

    Una vez teniendo todos estos pasos listos, ya se puede usar el código con normalidad.

**NOTAS IMPORTANTES:** 

¿Qué es Selenium? 

Selenium es una herramienta muy popular utilizada para la automatización de navegadores web. En Python, Selenium se usa comúnmente para realizar pruebas automáticas de aplicaciones web, raspar datos de sitios web, y automatizar tareas repetitivas en navegadores.

¿Por qué lo use para la elaboración de este proyecto? 

•	Carga dinámica de contenido: Muchas páginas web modernas, como la que estás interactuando (https://procesosjudiciales.funcionjudicial.gob.ec/busqueda-filtros), utilizan JavaScript para cargar contenido de manera dinámica. Esto significa que el contenido de la página no está presente en el HTML inicial que se recibe, sino que se carga después de que la página ha sido renderizada por el navegador.

•	Interacción con elementos: Para interactuar con los elementos de la página (como introducir datos en campos de texto, hacer clic en botones, etc.), es necesario utilizar un navegador que pueda ejecutar JavaScript y manejar estos elementos dinámicos. Selenium permite automatizar un navegador real (como Chrome) para realizar estas acciones.

Una vez entendido el porque de la implantación del código, es necesario explicar los Scripts:

Existen dos carpetas las cuales cada una tiene un Script.

La primera funciona para realizar Web Scraping a personas Naturales o Personas Jurídicas, COMO ACTOR/OFENDIDO

La primera, ‘Actor_Ofendido’:

Contiene el script ‘WebScrapingOfendido.py’ el cual carga la información en un archivo de formato .csv 

La segunda funciona para realizar Web Scraping a personas Naturales o Personas Jurídicas, COMO DEMANDADO/PROCESADO

Esta segunda contiene al igual que la primera el script con las mismas funciones del de la primera carpeta, pero para el caso del DEMANDADO.

Además de esto y como **PUNTO IMPORTANTE** , los scripts no llegan a extraer las actuaciones judiciales de cada proceso. Esto debido a un problema encontrado al momento de pasar de pagina en pagina en las tablas de los listados de procesos. 

Por qué **NO** un solo scripts para el DEMANDADO Y DEMANDANTE fue para mostrar tablas separadas las cuales se puedan convertir fácilmente en un DataFrame con Pandas y poder hacer un análisis mas sencillo. (En el video está un ejemplo de cómo se vería la información cargada en un DataFrame). 

Para esto hice un **video explicativo** donde hago una prueba con dos CC y el porqué de cómo están implementados los Scripts. 

Link video: https://drive.google.com/file/d/1Ody3SYiqZxL9zKh4vOTXiMqc4hE9KMhz/view?usp=sharing 

Espero que les guste lo que hice, **¡Gracias por su tiempo!**
