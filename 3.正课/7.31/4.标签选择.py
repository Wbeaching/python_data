from selenium import webdriver
from selenium.webdriver.common.by import By
import os,time


driver = webdriver.Firefox()
driver.get('file:///'+os.path.abspath('4.add.html'))
# 通过标签名字来找到指定标签
btns = driver.find_elements_by_tag_name('button')
print(btns)
btns[1].click()
# 1.通过索引来找到指定的标签
# for btn in btns:
#     #2. 通过属性来找到指定标签
#     if btn.get_attibute('type') == 'button':
#         btn.click()
# # for btn in btns:
#     time.sleep(3)
#     btn.click()
# driver .find_element_by_tag_name('button').click()
# find_element_by_XX 通过XX来找到所有标签中的第一个标签
# find_elements_by_XX 通过XX找到所有的符合标签
# 3.弹出指定的元素，如果不写索引，默认最后一个
# driver.find_elements_by_css_selector('button').pop().click()
# [type=button] []里面为限制条件 限制选择的内容
# driver.find_elements_by_css_selector('button[type=button]').pop().click()
# # 4.通过。。。来找到指定标签
# driver.find_element(by=By.ID,value='pink').click()
#






