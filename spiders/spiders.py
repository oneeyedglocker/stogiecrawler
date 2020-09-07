import scrapy


class MyPipeline(object):
    def process_item(self, item, spider):
        results.append(dict(item))


results = []


def spider_closed(spider):
    print(results)

class HoltsSpider(scrapy.Spider):
    name = 'holts'
    allowed_domains = ['holts.com']
    start_urls = ['http://www.holts.com/cigars/all-cigar-brands/cao-brazilia.html/']


    def parse(self, response):
        website_name = "holts"
        stogie_names = response.xpath('//tr[@class=""]')
        for stogie in stogie_names:
            stogie_name = stogie.xpath('.//div[@class="name"]/text()').get().strip()
            ring = stogie.xpath('.//span[@class="ring"]/text()').get().strip()
            quanity = stogie.xpath('.//*[@class="tpacking"]/span/text()').get().strip()
            price = stogie.xpath('.//*[@class="tprice "]/span/text()').get().strip()

            yield {
                    'website_name': website_name,
                    'stogie_name': stogie_name,
                    'stogie_ring': ring,
                    'stogie_quanity': quanity,
                    'stogie_price': price
            }



class FamousSpider(scrapy.Spider):
    name = 'famous'
    allowed_domains = ['famous-smoke.com']
    start_urls = ['https://www.famous-smoke.com/brand/cao-brazilia-cigars']


    def parse(self, response):
        website_name = "famous"
        stogie_names = response.xpath('//div[@class="brandcategory cigars"]//div[@class = "brandnewbox flexrow"]')
        for stogie in stogie_names:
            stogie_name = stogie.xpath('.//a[@class = "brandtitle"]/text()').get().strip()
            ring = stogie.xpath('.//div[@class = "brandspecs"]/text()').get().strip()
            quanity = stogie.xpath('.//div[@class = "right"]//span[@class="right pack"]/text()').get().strip()
            price = stogie.xpath('.//div[@class = "right"]//span[@class="right tar"]/b/text()').get().strip()

            yield {
                    'website_name': website_name,
                    'stogie_name': stogie_name,
                    'stogie_ring': ring,
                    'stogie_quanity': quanity,
                    'stogie_price': price
            }


class Cigar(scrapy.Spider):
    name = 'cigar'
    allowed_domains = ['cigar.com']
    start_urls = ['https://www.cigar.com/p/cao-brazilia-cigars/1411733/']


    def parse(self, response):
        website_name = "cigar"
        stogie_names = response.xpath('//div[@id="prod-groups"]//div[@class="prod-group"]')
        for stogie in stogie_names:
            stogie_name = stogie.xpath('.//div[@class="product-brand-heading"]/span[1]/text()').get().strip()
            ring = stogie.xpath('.//div[@class="product-brand-heading"]/span[3]/text()').get().strip()
            quanity = stogie.xpath('.//div[@class="row py-1 py-md-3 pl-md-2 border-bottom mx-0  prod-group-grid"]//span[@class="quantity-heading"]/text()') .get().strip()
            price = stogie.xpath('.//div[@class="row py-1 py-md-3 pl-md-2 border-bottom mx-0  prod-group-grid"]//span[@itemprop="price"]/text()').get().strip()

            yield {
                    'website_name': website_name,
                    'stogie_name': stogie_name,
                    'stogie_ring': ring,
                    'stogie_quanity': quanity,
                    'stogie_price': price
            }
