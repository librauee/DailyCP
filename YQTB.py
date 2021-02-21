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
driver.find_element_by_xpath('//*[@id="page"]/div/div/div/div/button[2]/span').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="emap-rsids-content"]/div/div[3]/div/div[1]/div/div/div/input').send_keys(USER_NAME)
driver.find_element_by_xpath('//*[@id="emap-rsids-content"]/div/div[3]/div/div[2]/div/div[1]/div/input').send_keys(USER_PASSWORD)
driver.find_element_by_xpath('//*[@id="emap-rsids-content"]/div/div[3]/div/div[3]/div/button/span').click()
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="xszm-search-in"]').send_keys('疫情')
driver.find_element_by_xpath('//*[@id="search-btn-input"]').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="xgpt-search-result-context"]/div/div[1]/div/a').click()
driver.implicitly_wait(10)

windows = driver.window_handles
driver.switch_to.window(windows[-1])
driver.find_element_by_xpath('//*[@id="save"]').click()

