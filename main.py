from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome("/Applications/chromedriver")
files=open('HUH_rec.csv').readlines()

def scraper(family,collection_ID):
	driver.get("http://www.cvh.ac.cn/spms/list.php?taxonName=&family="+family+"&genus=&country=&county=&locality=&altitude=&recordedBy=&recordNumber="+collection_ID+"&year=&collectionCode=&identifiedBy=&dateIdentified=“)
	soup = BeautifulSoup(driver.page_source)
	result=soup.find_all('tr',attrs={'class':'spms-row'})
	result[0].attrs['data-collection-id']
	driver.get("http://www.cvh.ac.cn/spms/info.php?id="+ result[0].attrs['data-collection-id’])
	soup = BeautifulSoup(driver.page_source)
	sp_nam=soup.find_all('td',attrs={'id':'formattedName’})[0].contents

for line in files:
	scraper(line)