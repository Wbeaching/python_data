from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
# 获取当前的window对象
current_window = driver.current_window_handle
# 获取当前网页的标题
print(current_window)

driver.find_element_by_name('tj_trnews').click()
news = WebDriverWait(driver,5).until(lambda driver:driver.find_element_by_css_selector('.hdline0.a3'))
news.click()
# print(news)

all_windows = driver.window_handles
print(all_windows)
for window in all_windows:
    if window != current_window:
        # switch 切换
        driver.switch_to.window(window)
title = driver.find_element_by_tag_name('h1').text
WebDriverWait(driver,5).until(lambda driver:title.is_display)
# title = driver.find_element_by_css_selector('.text_title > h1').text
print(title)
# 关闭浏览器
driver.quit()
# 关闭窗口
time.sleep(3)
driver.close()
driver.switch_to.window(current_window)
print(driver.find_element_by_css_selector('#footer span').text)



