# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join

def remover_espaco_em_branco(text):
    return text.strip()

def processar_caracteres_especiais(text):
    return text.replace(u'\u201c', '').replace(u'\u201d', '').replace(u'\u2014', '-')

class DesafioGoodReadsItem(scrapy.Item):
    frase = scrapy.Field(
        input_processor = MapCompose(
            remover_espaco_em_branco, processar_caracteres_especiais),
        output_processor = TakeFirst()
    )
    autor = scrapy.Field(
        output_processor = TakeFirst()
    )
    tags = scrapy.Field(
        output_processor = Join(", ")
    )
