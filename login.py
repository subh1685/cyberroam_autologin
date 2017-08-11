from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chromedriver='c:/Users/Alpha/Downloads/chromedriver.exe'
browser=webdriver.Ie(chromedriver)
browser.get('https://172.16.1.1:8090/httpclient.html?u={proto}{url}')
username=browser.find_element_by_name('username')
password=browser.find_element_by_name('password')
username.send_keys('be1061514')
password.send_keys('subh1685')
login=browser.find_element_by_id('logincaption')
login.submit()





