# Claro CellPhone

## 1. Definición del Problema

### 🤔 ¿Cuál es el problema que queremos resolver?

Evaluar los dispositivos disponibles en la tienda Claro Colombia para informar a los interesados que deseen renovar o adquirir, ayudándoles a tomar decisiones informadas sobre sus compras.

## 2. Definición de los Objetivos

### 🎯 ¿Qué queremos conseguir con el proyecto?

Comparar dispositivos de Claro Colombia por marca para ayudar a los compradores a elegir la mejor opción en función de sus características y precios.

## 3. Recolección de Datos

### 💾 ¿De dónde obtenemos los datos que necesitamos?

Los datos se obtuvieron a través de un proceso de Web Scraping desde las siguientes páginas:

- [Claro Colombia](https://tienda.claro.com.co/claro/celulares)
- [Claro Paraguay](https://tienda.claro.com.py/)

#### Características extraídas de cada dispositivo:

1. **`Dispositivo`:** Nombre o modelo del dispositivo móvil.
2. **`Precio`:** Precio del dispositivo en la moneda local del país de origen.
3. **`Marca`:** Marca del dispositivo (Samsung, Apple, Huawei, etc.).
4. **`RAM`:** Cantidad de memoria RAM en gigabytes (GB).
5. **`Memoria Interna`:** Capacidad de almacenamiento interno en gigabytes (GB).
6. **`Cámara Frontal`:** Especificaciones de la cámara frontal del dispositivo.
7. **`Cámara Trasera`:** Especificaciones de la cámara trasera del dispositivo.
8. **`Batería`:** Capacidad de la batería en miliamperios-hora (mAh).
9. **`Sistema Operativo`:** Sistema operativo que utiliza el dispositivo (Android, iOS, etc.).
10. **`Tamaño de Pantalla`:** Tamaño de la pantalla del dispositivo en pulgadas.

## 4. Limpieza de Datos

### 🧹 ¿Cómo preparamos los datos para el análisis?

Se realizó una limpieza de datos en Excel (PowerQuery) para eliminar valores no deseados y datos incompletos, asegurando que los datos estén listos para el análisis.

# Instrucciones para Ejecutar el Proyecto

1. **Crear Entorno en Windows y Linux:**
   
   ```bash
   python -m venv env
   ```

2. **Instalar Dependencias en el Entorno:**
   
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar el Spider de Scrapy:**
   
   ```bash
   scrapy runspider tu_spider.py -o archivo_salida.csv -t csv --set CLOSESPIDER_ITEMCOUNT=X
   ```
   
   - `tu_spider.py`: Nombre del archivo que contiene el spider.
   - `-o archivo_salida.csv`: Nombre del archivo de salida para almacenar los datos raspados.
   - `-t csv`: Formato en el que se guardarán los datos raspados (en este caso, CSV).
   - `--set CLOSESPIDER_ITEMCOUNT=X`: Opcional - Limita la cantidad de elementos que se raspan (reemplaza `X` con el número deseado).

## Automatización con Selenium

Para detalles sobre cómo automatizar el proceso con Selenium, consulta la [documentación de Selenium en Python](https://selenium-python.readthedocs.io/getting-started.html).
