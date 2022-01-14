from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time

def web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("no-sandbox")
    options.add_argument('--dns-prefetch-disable')
    options.add_argument("--disable-extensions")
    return webdriver.Chrome(executable_path='D:/chromedriver_96/chromedriver.exe')

def data_scraper():  

    all_links = []
    while True:
        soup = BeautifulSoup(driver.page_source,features='lxml')
        links = soup.find_all('div',{'class':'yuRUbf'})
        for j in links:
            data = j.find('a').get('href')
            print('Scraper is Running! Number of links ---> ',len(all_links))
            data_dict = {
                'Links':data
            }
            all_links.append(data_dict)
            df =  pd.DataFrame(all_links)
            df.to_csv(f'{input_keywrd}_Links.csv')
        try:
            next = driver.find_element(By.XPATH,
            '//*[@id="pnnext"]/span[2]')
        except:
            pass
        try:
            if next:
                next.click()   
                time.sleep(2)
        except:
            break
    print('All Results Scraped')    
    driver.close()
            
if __name__ =='__main__':
    driver = web_driver()
    url = 'https://www.google.com/'
    driver.get(url)
    input_keywrd = input('Enter Your Keyword: ')
    time.sleep(2) 
    search_box = driver.find_element(By.XPATH,
        '/html//form//div//div[2]/input')
    search_box.click()
    search_box.send_keys(input_keywrd) 
    time.sleep(1)
    search_box.send_keys('\ue007') 

    data_scraper()
    
      




