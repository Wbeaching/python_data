from selenium import webdriver
import os
driver = webdriver.Firefox()
driver.get('file:///'+os.path.abspath('6.outfram.html'))
# driver.switch_to.frame(driver.find_element_by_id('out'))
# driver.switch_to.frame('in')
# driver.find_element_by_id('kw').send_keys('selenium')
# driver.find_element_by_id('su').click()


