# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from scrapy.selector import Selector #'THIS USES HTML PARSER TO PARSE THE WEB

#This project will scrapte the amazon site and get the name of the item and its price

class MultipleSpider(scrapy.Spider):
    name = 'multiple'#name of our spiyder
    
    #The following is the domain(sites) and the start urls.
    #The start_requests is the way scrapy will request all the urls
    allowed_domains = ['amazon.com']
    #The following is the urls that we scrape.
    start_urls = ['https://www.amazon.co.uk/s/ref=sr_pg_1?fst=as%3Aon&rh=k%3Aheadphones%2Cn%3A560798&keywords=headphones&ie=UTF8&qid=1553447552',
                'https://www.amazon.co.uk/s/ref=sr_pg_2?fst=as%3Aon&rh=k%3Aheadphones%2Cn%3A560798&page=2&keywords=headphones&ie=UTF8&qid=1553447541',
               "https://www.amazon.co.uk/s?k=headphones&i=electronics&rh=n%3A560798&page=3&qid=1553655220&ref=sr_pg_3"]
    #The follwoing function calls to those urls
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)
        
      
     #THE FOLLOWING IS EXTRACTING THE NAME AND PRICE OF THE ITEMS IN SCRAPY 

    def parse(self, response):
        xxs = Selector(response) #YOU CAN USE XML OR HTML TO PARSE THE WEB.WE ARE USING HTML HERE CUZ WE PARSING A HTML SITE NOT XML
        
        price=xxs.xpath('//span[@class="a-size-base a-color-price s-price a-text-bold"]/text()').extract()#This will scrapte the prices of items
        title=xxs.xpath('//h2[@class="a-size-base s-inline s-access-title a-text-normal"]/text()').extract()#This will scrapte title of items
       
                
        dic = dict(zip(title, price))#We will put them both in a dictionary which is easy to read
        
        for idx, val in enumerate(price):#THIS IS HOW WE MAKE A FUNICTION and will combine multiple pages of data into the dic we made earlier
            dic[title[idx]]=val
          
        cols = ['item', 'price']#WE ARE NOT CONVERTING TO DF CUZ IT MAKES IT EASIER TO THEN CONVERT TO CSV
        #dat = pd.DataFrame(columns = cols)
        #for key,value in dic.items():
         #   dat = dat.append({'item': str(key), 'price':value},ignore_index=True) #convering to dataframe.So we can do analysis on the prices later
            
        
        
        yield dic #print it out in command line
       
        dat.to_csv("2scrapedpages1.csv", encoding='utf-8', index=False)#now we have madea  dataset and will be converted to CSV.
        
