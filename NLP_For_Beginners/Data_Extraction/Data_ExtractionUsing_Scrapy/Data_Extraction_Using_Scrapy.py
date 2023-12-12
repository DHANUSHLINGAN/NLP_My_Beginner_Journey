#Use the environment nlpr
#Scrapy is a python framework for a large scale web scraping
#
#Provides the tool required to efficiently extract data from websites,process them and Store them in your Preferred Structure and format

#scrapy startproject bookscraper


#Bookscraper(Folders)
# Spiders = Contains all the future scrapy files used to exract the data
# items.py = it is a abstraction layer to store the scrap data within the scrapy frame work
# middlewaares.py = how scrapy runs and makes the request to the servers(we can modify it)
# pipelines = Any data processing like cleaning,organization,droping etc  after the extraction
# settings.py = how scrapy should run (What should be the delay between the requests- If there are multi) ,caching and file downloading many more



# Spiders folder(All the scrapy files that used to extract data)
# Create a bookscraper.py
# After the code completion run "scrapy crawl bookscraper"


