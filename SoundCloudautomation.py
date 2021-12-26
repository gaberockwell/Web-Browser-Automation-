import os 
from selenium import webdriver
import platform
from selenium.webdriver.chrome.options import Options


track_link_xpath= '//*[@id="content"]/div/div[3]/div/div[1]/ul/li[3]/a'
soundcloud_play_xpath = '//*[@id="content"]/div/div[4]/div[1]/div/div[2]/div/ul/li[1]/div/div/div[2]/div[1]/div/div/div[1]/a'


options = Options()
options.page_load_strategy = 'eager'

def soundcloud():
	driver = webdriver.Safari()
	driver.get("https://soundcloud.com/youngxerc")
	driver.find_element_by_xpath(track_link_xpath).click()
	driver.implicitly_wait(3)
	driver.find_element_by_xpath(soundcloud_play_xpath).click()

soundcloud()



















"""younghefe_play_xpath = '//*[@id="content"]/div/div[4]/div[1]/div/div[2]/div/div[1]/div[3]/ul/li[1]/div/div/div/div[2]/div[1]/div/div/div[1]/a'




def younghefe():
	driver.get('https://soundcloud.com/youngxerc')
	driver.find_element_by_xpath(younghefe_play_xpath).click()
	time.sleep(3)

 
younghefe()"""