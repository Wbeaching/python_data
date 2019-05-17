# selenium 由网页驱动驱使浏览器操作，特点：速度慢
# 经常出现代码执行完了，但是网页内容还没有加载完毕
# 里面的标签没有显示出来，如果这时候操作里面的标签就会爆出异常
# 解决办法：时间休眠
# 不管页面的内容有没有加载完毕，一定要加载指定的秒数

from selenium.webdriver.support.ui import  WebDriverWait
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
# driver.find_element_by_id('kw').send_keys('hello world')
button = driver.find_element_by_id('su')
# webdriverwait 网页等待
# 值1：等待对形象
# 值2：等待时间
# WebDriverWait经常和until以及until not使用
# lambda 匿名函数   is_displayed是否已经显示
is_visible = WebDriverWait(driver,10).until(lambda driver:button.is_displayed())
print(is_visible)
button.click()

# WebDriverWait和time.sleep()
# 1.都是让程序等待执行的时间
# 2.time的时间是固定的，时间长短不会随着标签的加载速度而改变
# WebDriverWait时间是不固定的，等待多少时间要看标签的加载时间和制定的过顶时间
# 3.如果在指定的时间内，标签仍没有加载出来，那么time和WebDriverWait都会曝出异常

# 隐形时间 implicility_wait