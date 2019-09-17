# selenium 硒
# selenium 是一个自动化测试工具
# 手动测试
# 自动测试
# 白盒测试
# 黑盒测试
# 在python中的应用：

# selenium 可以完全模拟人对浏览器操作，对动态数据进行获取
# 1.动态数据由代码生成，在页面初始化的过程中是没有的
# 也无法获取，但是可以通过selenium来获取
# 2.有些数据是需要进行登陆以后才能获取，比如说
# 好友列表，评论，消费记录...登陆以后获取cookie
# 才能进行以上操作，但是使selenium 以后，可以
# 避免人工登录，只需要得到账号密码即可实现selenium代替登陆
# selenium的特点
# 1.由程序控制浏览其进行操作，而不是手动操作浏览器
# 2.程序控制浏览器操作的时候，速度非常慢，所以要谨慎使用selenium
# 3.使用selenium控制浏览器的时候，需要下载浏览到对应的控制程序
# 4.selenium为开源，免费，但是更新速度没有浏览器快，不是selenium更新慢
#   而是浏览器更新快，要注意浏览器与selenium之间的关系
# 引入网页驱动
from selenium import webdriver
import time
# 使用网页驱动来运行火狐浏览器
driver = webdriver.Firefox()
# 通过驱动来执行指定的网页
driver.get('http://www.baidu.com')

# selenium 提供了找到元素的方法 find_element_by_xxxxx
# 这些方法全部都是用python实现的
# 如果只是想对这个元素进行查找，定位，建议使用
# xpath 或者 css_selector
# 如果需要对找到的内容进行点击操作
# 建议使用find_element_by_xxx
# find 找到 element 元素 by 通过
#
# 错误原因：代码执行速度很快，但浏览器响应很慢
# 代码执行到这的时候，浏览器里面的元素可能还没有加载完
# 所以报错找不到指定的元素
time.sleep=5
driver.find_element_by_id('kw').send_keys('selenium')
# 通过name值来找
driver.find_element_by_name('wd').send_keys('csdn')
driver.find_element_by_class_name('s_ipt').send_keys(u'智游')
# tag__name标签名
driver.find_element_by_tag_name('input').send_keys('cctv')
# 前端
# html
# css
# js
# selector 样式选择器 #id .类名
driver.find_element_by_css_selector('#kw')
# 通过xpath语法定位一个元素
driver.find_element_by_xpath('//form[@id="form"]/span/input[@id="kw"]')
# 通过页面文本按钮找到它的url
driver.find_element_by_link_text('贴吧')

# time.sleep(1)
driver.close()



