from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.selector import Selector
import re

# Paso 1: Definimos la estructura de datos para almacenar información de los teléfonos. 📱
class PhoneFeatures(Item):
    device = Field()
    price = Field()
    brand = Field()
    ram = Field()
    internal_memory = Field() 
    frontal_camera = Field() 
    rear_camera = Field() 
    battery = Field()  
    operating_system = Field()  
    display_size = Field() 

# Paso 2: Definimos la araña de rastreo de CrawlSpider. 🕷️
class ClaroSpider(CrawlSpider):
    name = "claro"
    start_urls = ['https://tienda.claro.com.co/claro/celulares']
    allowed_domains = ['tienda.claro.com.co']

    rules = (
        Rule(LinkExtractor(allow=r'beginIndex=(24|48|72)(&|$)'), follow=True),
        Rule(LinkExtractor(allow=r'/claro/celulares/'), callback='parse_item', follow=True),
    )

    # Paso 3: Definimos el método para analizar y extraer datos de la página web.
    def parse_item(self, response):
        # Paso 4: Creamos un cargador de elementos para almacenar la información extraída.
        loader = ItemLoader(item=PhoneFeatures(), selector=response)

        # Paso 5: Mapeamos nombres de atributos a campos en la clase PhoneFeatures.
        attribute_mapping = {
            "RAM:": 'ram',
            "Memoria interna:": 'internal_memory',
            "MPX Cámara Frontal:": 'frontal_camera',
            "MPX Cámara Principal:": 'rear_camera',
            "Batería:": 'battery',
            "Sistema operativo:": 'operating_system',
        }

        # Paso 6: Extraemos información de atributos adicionales del dispositivo.
        attributes = response.xpath('//div[@id="descAttrTextContainer"]/ul/li')
        for attribute in attributes:
            name = attribute.xpath('span[starts-with(@id, "descAttributeName_")]/text()').get()
            value = attribute.xpath('span[starts-with(@id, "descAttributeValue_")]/text()').get()

            if name:
                name = name.strip()
                # Paso 7: Verificamos si el nombre del atributo está en nuestro mapeo.
                if name in attribute_mapping:
                    # Paso 8: Obtenemos el nombre del campo correspondiente en PhoneFeatures.
                    field_name = attribute_mapping[name]
                    # Paso 9: Agregamos el valor al campo en el cargador de elementos.
                    loader.add_value(field_name, value.strip() if value else 'N/A')

        # Paso 10: Extraemos otros campos como el nombre del dispositivo, el precio, la marca y el tamaño de la pantalla. 
        loader.add_xpath('device', '//*[@id="PageHeading_30458"]/h1/text()')
        price_text = response.xpath('//div//span[starts-with(@id, "offerPrice_")]/text()').get()
        loader.add_value('price', re.sub(r'[^\d.$]', '', price_text))
        brand = Selector(response).xpath('//span[starts-with(@id, "product_manufacturer_")]/text()').get()
        loader.add_value('brand', brand.strip())
        pantalla_text = response.xpath('//span[contains(text(), "Tamaño de Pantalla")]/following-sibling::span[@class="attrDescription"]/text()').get()
        loader.add_value('display_size', pantalla_text.strip() if pantalla_text else 'N/A')

        # Paso 11: Devolvemos el objeto cargado con los datos extraídos.
        yield loader.load_item()
