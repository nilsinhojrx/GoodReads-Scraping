import scrapy
from scrapy.loader import ItemLoader
from desafio_good_reads.items import DesafioGoodReadsItem


class GoodReadsSpider(scrapy.Spider):
	# Identidade
    name = "goodbot"
		# Requests
    def start_requests(self):
        urls = ['https://www.goodreads.com/quotes']
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    # Response
    def parse(self, response):
        # processar a resposta
        for elemento in response.xpath("//div[@class='quoteDetails']"):
            # Criar classe Item Loader:
            loader = ItemLoader(item = DesafioGoodReadsItem(),
                       selector = elemento,
                       response = response
                    )
            loader.add_xpath("frase", ".//div[@class='quoteText']/text()")
            loader.add_xpath("autor", ".//div[@class='quoteText']//span[@class='authorOrTitle']/text()")
            loader.add_xpath("tags", ".//div[@class='greyText smallText left']/a/text()")

            yield loader.load_item()
            
        # paginação
        try:              
          link_next = response.xpath("//a[@class='next_page']/@href").get()
          if link_next is not None:
              link = response.urljoin(link_next)
              yield scrapy.Request(url = link, callback = self.parse)
        except:
            print(f"Todas as páginas foram varridas ! \n")