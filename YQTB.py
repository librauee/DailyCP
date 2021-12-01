from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from Config import *

chrome_options = Options()
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)
driver.get("http://stu.hfut.edu.cn/")
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="page"]/div/div/div/div/button[1]/span').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="username"]').send_keys(USER_NAME)
driver.find_element_by_xpath('//*[@id="pwd"]').send_keys(USER_PASSWORD )
driver.find_element_by_xpath('//*[@id="sb2"]').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="xgpt-xszp-body-cyyy"]/div/div[2]/div[1]/div[1]/img').click()
driver.implicitly_wait(5)
windows = driver.window_handles
driver.switch_to.window(windows[-1])
driver.find_element_by_xpath('//*[@id="save"]').click()
driver.implicitly_wait(5)
driver.find_element_by_link_text("确认").click()

