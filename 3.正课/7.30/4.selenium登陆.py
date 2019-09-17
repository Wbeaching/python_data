
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('https://i.meishi.cc/login.php?redirect=https%3A%2F%2Fwww.meishij.net%2F')

driver.find_element_by_name('username').send_keys('2963079730@qq.com')

driver.find_element_by_class_name('password').send_keys('199606184810zuo')
time.sleep(3)
username = driver.find_element_by_name('username').text
password = driver.find_element_by_class_name('password').text
print(username)
print(password)
driver.find_element_by_name('username').clear()
driver.find_element_by_class_name('password').clear()
driver.find_element_by_xpath('//div[@class="msj_loginbox"]/input[@class="submit"]').click()