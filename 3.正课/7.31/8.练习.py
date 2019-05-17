from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
# driver = webdriver.Firefox()
# driver.get('https://i.meishi.cc/login.php?redirect=https%3A%2F%2Fwww.meishij.net%2F')
# driver.find_element_by_name('username').send_keys('2963079730@qq.com')
# driver.find_element_by_name('password').send_keys('199606184810zuo')
# driver.find_element_by_xpath('//div[@class="nl_loginitem"]/input[@class="submit"]').click()
# driver.find_element_by_link_text('菜谱大全').click()
# driver.find_element_by_link_text('孕妇').click()
# # for page in range(1,2):
# #     print('正在爬去第{}页数据'.format(page))
# for row in range(1,7,2):
#     x = float(row)/6
#     js = 'document.documentElement.scrollTop=document.documentElement.scrollHeight *%f'% x
#     driver.execute_script(js)
#     time.sleep(3)
# item_list = driver.find_elements_by_id('listtyle1_list')
# print(item_list)
# for item in item_list:
#     with open('meishi.txt','a',encoding='utf-8') as f:
#         f.write(item.text)
#         f.write('\n')
# 查找某个元素建议使用xpath 或者 css_selector
# 如果要对找到的内容进行点击操作
# 建议使用find_element_by_XXX
# tag_name 标签名
# driver = webdriver.Firefox()
# driver.get('https://i.meishi.cc/login.php?redirect=https%3A%2F%2Fwww.meishij.net%2F')
# driver.find_element_by_name('username').send_keys('')
# driver.find_element_by_class_name('password').send_keys('')
# time.sleep(2)
# username = driver.find_element_by_xpath('//div[@class="msj loginbox"]/input[@class="submit"').click()
driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
driver.find_element_by_id('kw').send_keys(u'爬虫技巧')
driver.find_element_by_id('su').click()
# 退出浏览器
# driver.quit()
# WebDriverWait(driver,5) .unti(lambda driver:driver.find_element_by_id('su'))
# logo = driver.find_element_by_css_selector('#lg>img')
# WebDriverWait(driver,5).until(lambda driver:logo.is_displayed())
# ActionChains(driver).double_click(logo).perform()
# action = ActionChains(driver).context_click(logo).perform()
# ActionChains(driver).move_to_element(action).perform()
# driver.get('http://www.baidu.com')
# btns_list = driver.find_element_by_tag_name('button')
# btns_list[1].click()
# for btn in btns_list:
#     if btn.get_attibute('type') == 'button':
#         btn.click()
# driver = webdriver.Firefox()
# driver.get('')
# driver.find_element_by_name('username').send_keys('')