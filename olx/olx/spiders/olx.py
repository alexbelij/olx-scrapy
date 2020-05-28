import scrapy

class CoinMarket(scrapy.Spider):
    name = "olx"
    start_urls = ['https://www.olx.ua/transport/avtomobili-iz-polshi/' + str(f'?page={i}') for i in range (1, 2)]

    def parse(self, response):
        links = response.xpath('//*[@id="offers_table"]/tbody/tr/td/div/table/tbody/tr[1]/td[1]//a/@href').getall()
        yield from response.follow_all(links, self.parse_data)


    def parse_data(self, response):
        text = response.xpath('//*[@id="offerdescription"]/div[1]/h1//text()').get()
        price = response.xpath('//*[@id="offerdescription"]/div[1]/div[2]/div/strong//text()').get()
        type_ad = response.xpath('//*[@id="offerdescription"]/div[2]/ul/li[1]/a/strong//text()').get()
        car_brand = response.xpath('//*[@id="offerdescription"]/div[2]/ul/li[2]/a/strong//text()').get()
        model = response.xpath('//*[@id="offerdescription"]/div[2]/ul/li[3]/a/strong//text()').get()
        year = response.xpath('//*[@id="offerdescription"]/div[2]/ul/li[4]/span/strong//text()').get()
        fuel = response.xpath('//*[@id="offerdescription"]/div[2]/ul/li[5]/a/strong//text()').get()
        mileage = response.xpath('//*[@id="offerdescription"]/div[2]/ul/li[6]/span/strong//text()').get()
        body_type = response.xpath('//*[@id="offerdescription"]/div[2]/ul/li[7]/a/strong//text()').get()
        country_city = response.xpath('//*[@id="offerdescription"]/div[2]/ul/li[8]/span/strong//text()').get()
        colour = response.xpath('//*[@id="offerdescription"]/div[2]/ul/li[9]/a/strong//text()').get()
        status = response.xpath('//*[@id="offerdescription"]/div[2]/ul/li[10]/a/strong//text()').get()
        transmission = response.xpath('//*[@id="offerdescription"]/div[2]/ul/li[11]/a/strong//text()').get()
        views = response.xpath('//*[@id="offerbottombar"]/ul/li[2]/span/strong//text()').get()
        url = response.url
        yield {
             'Auto': car_brand,
             'Type ad': type_ad,
             'Model': model,
             'Year': year,
             'Mileage': mileage,
             'Fuel': fuel,
             'Colour': colour,
             'Body type': body_type,
             'Price': price,
             'Status': status,
             'Transmission': transmission,
             'Text': text,
             'Country-City': country_city,
             'Views': views,
             'Link url': url


        }
