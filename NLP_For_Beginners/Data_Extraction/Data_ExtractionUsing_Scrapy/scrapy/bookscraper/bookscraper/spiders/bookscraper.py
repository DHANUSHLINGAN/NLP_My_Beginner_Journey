from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from bookscraper.items import BookscraperItem
import os
from csv import writer

class BookScraper(CrawlSpider):
    name = "bookscraper"
    start_urls = ["https://books.toscrape.com/"]
    rules = (
        Rule(LinkExtractor(restrict_css = ".nav-list > li > ul > li > a "), follow = True),#Start Iterating over the Categories pages using the css selector
        Rule(LinkExtractor(restrict_css = ".product_pod > h3 > a"),callback="parse_book")
        )
    
    #Extracter Phase
    def parse_book(self,response):
        book_item = BookscraperItem()
        book_item["image_url"] = response.urljoin(response.css(".item.active > img::attr(src)").get())
        book_item["title"] = response.css(".col-sm-6.product_main > h1 ::text").get()
        book_item["price"] = response.css(".table.table-striped > tr:nth-child(1) > td::text").get()
        book_item["upc"] = response.css(".table.table-striped > tr:nth-child(1) > td::text").get()
        book_item["url"] = response.url
        self.Save_to_file(book_item["image_url"],book_item["title"],book_item["price"],book_item["upc"],book_item["url"])
        return book_item
    
    #Storage Phase
    def Save_to_file(self,image_url,title,price,upc,url):
        #Create and open a file by the name data in write mode
        #encoding ensures that special characters are properly extracted from the page 
        self.price = price
        self.image_url = image_url
        self.title = title
        self.upc = upc
        self.url = url
        if os.path.isfile("data.csv"):
            with open('data.csv' ,'a') as f_object :
                writer_object =   writer(f_object)

                #Pass a list as an argument into
                #the writerow()
                writer_object.writerow([self.image_url,self.title,self.price,self.upc,self.url])
                #Close the file object
                f_object.close()
        else :
            with open('data.csv','w') as f_object:
                writer_object = writer(f_object)

                #Pass the list as an argument into 
                #the writerrow()
                writer_object.writerow([self.image_url,self.title,self.price,self.upc,self.url])
                #Close the file Object
                f_object.close()

