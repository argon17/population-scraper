import scrapy
import pdb

class CountriesSpider(scrapy.Spider):
    name = "countries"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country"]

    def parse(self, response):
        countries = response.xpath("//td/a")
        for country in countries:

            #  get() is for getting string type
            name = country.xpath(".//text()").get()
            relative_url = country.xpath(".//@href").get()

            # absolute_url = f"https://www.worldometers.info{relative_url}"
            # absolute_url = response.urljoin(relative_url)
            # yield response(url=absolute_url)

            yield response.follow(url=relative_url, callback=self.parse_country, meta = {"country_name" : name})

    def parse_country(self, response):
        name = response.meta["country_name"]
        rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()
            yield {
                'country_name': name,
                'year': year,
                'population': population
            }