#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from Common.baseui import baseUI

from selenium import webdriver


class TestUI:


    def start(self):
        # 确定chromedriver.exe的位置
        driver_path = os.path.join(os.path.dirname(__file__), "../../chromedriver/chromedriver.exe")
        # 打开浏览器
        driver = webdriver.Chrome(driver_path)
        driver.maximize_window()  # 最大化浏览器
        driver.set_page_load_timeout(10)  # 网页加载超时为10s
        driver.set_script_timeout(10)  # js脚本运行超时10s
        driver.implicitly_wait(10)  # 元素查找超时时间10s
        return driver

    def quit(self,driver):
        driver.quit()

    def test_demo1(self):
        driver = self.start()
        driver.get("https://www.baidu.com")
        time.sleep(2)   #休眠2秒
        driver.back()  #后退
        time.sleep(2)  # 休眠2秒
        driver.forward() #前进
        time.sleep(2)  # 休眠2秒
        driver.refresh() #刷新
        time.sleep(2)  # 休眠2秒
        self.quit(driver)
    def test_page(self):
        driver = self.start()
        driver.get("D:\\software\\apache-tomcat-7.0.79\\webapps\\xuepl\\demo1.html")
        #定位文本输入框//td[contains(text(),'text:文本输入框')]/following-sibling::td//input
        text = driver.find_element_by_xpath("//td[contains(text(),'text:文本输入框')]/following-sibling::td//input")
        #清空
        text.clear()
        #输入
        text.send_keys("对不对？对！")

        # #定位文件上传框//td[contains(text(),'file:文件上传框')]/following-sibling::td//input
        # file = driver.find_element_by_xpath("//td[contains(text(),'file:文件上传框')]/following-sibling::td//input")
        # # 清空
        # file.clear()
        # # 输入
        # file.send_keys("‪D:\\software\\apache-tomcat-7.0.79\\webapps\\xuepl\\demo.html")

        #定位第一个单选框//td[contains(text(),'radio:单选框')]/following-sibling::td//input[1]
        # radio = driver.find_element_by_xpath("//td[contains(text(),'radio:单选框')]/following-sibling::td//input[2]")
        # #点击
        # radio.click()
        #
        #
        # #定位第一个多选框//td[contains(text(),'checkbox:多选框')]/following-sibling::td//input[1]
        # checkbox = driver.find_element_by_xpath("//td[contains(text(),'checkbox:多选框')]/following-sibling::td//input[1]")
        # #点击
        # checkbox.click()
        # time.sleep(2)
        # checkbox.click()
        # print(type(checkbox))
        # time.sleep(2)
        # #全选//td[contains(text(),'checkbox:多选框')]/following-sibling::td//input
        # checkboxes = driver.find_elements_by_xpath("//td[contains(text(),'checkbox:多选框')]/following-sibling::td//input")
        # for c in checkboxes:
        #     c.click()
        # time.sleep(2)
        #
        # #定位按钮//td[contains(text(),'button:普通按钮')]/following-sibling::td//input
        # driver.find_element_by_xpath("//td[contains(text(),'button:普通按钮')]/following-sibling::td//input").click()
        # #定位日期控件//td[contains(text(),'date:日期控件')]/following-sibling::td//input
        # # date = driver.find_element_by_xpath("//td[contains(text(),'date:日期控件')]/following-sibling::td//input")
        #
        # base = baseUI(driver)
        # base.update_attribute_by_xpath("修改日期控件的值","//td[contains(text(),'date:日期控件')]/following-sibling::td//input","value","2019-04-29")
        #
        #
        # #定位文本输入域//td[contains(text(),'textarea:文本输入区')]/following-sibling::td//textarea
        # textarea = driver.find_element_by_xpath("//td[contains(text(),'textarea:文本输入区')]/following-sibling::td//textarea")
        # #清空
        # textarea.clear()
        # #输入
        # textarea.send_keys("我是谁？我在哪？")


        #定位下拉框//td[contains(text(),'select:下拉框')]/following-sibling::td//select
        # select = driver.find_element_by_xpath("//td[contains(text(),'select:下拉框')]/following-sibling::td//select")
        # #点击下拉框
        # select.click()
        # #定位下拉框选项//td[contains(text(),'select:下拉框')]/following-sibling::td//select/option[1]
        # option = driver.find_element_by_xpath(
        #     "//td[contains(text(),'select:下拉框')]/following-sibling::td//select/option[2]")
        # #点击下拉框选项
        # option.click()

        # s = Select(select)
        # #通过索引选择
        # s.select_by_index(2)
        # time.sleep(2)
        # #通过value属性的值选择
        # s.select_by_value("z1")
        # time.sleep(2)
        # #通过展示文本选择
        # s.select_by_visible_text("周龙3")

        #定位超链接//td[contains(text(),'a:超链接')]/following-sibling::td//a
        # a = driver.find_element_by_xpath("//td[contains(text(),'a:超链接')]/following-sibling::td//a")
        #点击
        # time.sleep(2)
        # a.click()
        #ctrl+点击   按下ctrl   点击   松开ctrl
        #实例化ActionChains类   ActionChains封装了所有的鼠标键盘的操作


        #
        # action.key_down(Keys.CONTROL).click(a).key_up(Keys.CONTROL).perform()
        #
        # #shift+点击
        # action.key_down(Keys.SHIFT).click(a).key_up(Keys.SHIFT).perform()

        # driver.get("https://www.jianshu.com/")
        # time.sleep(1)
        # #滚动一定距离
        # # js="var q=document.documentElement.scrollTop=10000"
        # # driver.execute_script(js)
        # time.sleep(1)
        # #滚动到某个元素//div[@id='list-container']/ul/li[1]
        # a = driver.find_element_by_xpath("//div[@id='list-container']/ul/li[5]")
        # js = "arguments[0].scrollIntoView();"
        # driver.execute_script(js,a)

        #定位超链接//td[contains(text(),'a:超链接')]/following-sibling::td//a
        # aes = driver.find_elements_by_xpath("//td[contains(text(),'a:超链接')]/following-sibling::td//a")
        #
        # for a in aes:
        #     action = ActionChains(driver)
        #     action.key_down(Keys.CONTROL).click(a).key_up(Keys.CONTROL).perform()
        #     time.sleep(1)

        #获取所有窗口句柄
        # handles = driver.window_handles
        # #使用foreach循环，获取每个窗口的句柄
        # for handle in handles:
        #     #窗口切换至目标句柄的窗口
        #     driver.switch_to.window(handle)
        #     #判断当前窗口的title是否包含“当当”，如果包含就退出循环
        #     if(driver.title.__contains__("当当")):
        #         break
        #     time.sleep(1)
        #定位弹框按钮//td[contains(text(),'button:普通按钮')]/following-sibling::td//input
        # driver.find_element_by_xpath("//td[contains(text(),'button:普通按钮')]/following-sibling::td//input").click()
        # time.sleep(1)
        # #切换窗口至弹框
        # alert = driver.switch_to.alert
        # #输入
        # alert.send_keys("周龙")
        # time.sleep(1)
        # print(alert.text)
        # #确认
        # alert.accept()
        #取消
        # alert.dismiss()
        driver.get("http://www.guoyasoft.com:8080/guoya-client/jsp/user/login.jsp")
        time.sleep(1)
        username = driver.find_element_by_xpath("//input[@id='userName']")
        username.clear()
        username.send_keys("xuepl")
        password = driver.find_element_by_xpath("//input[@id='password']")
        password.clear()
        password.send_keys("123456")
        driver.find_element_by_xpath("//input[@id='loginBtn']").click()
        time.sleep(5)
        button = driver.find_element_by_xpath("//a[contains(text(),'面试查询')]")
        button.click()
        time.sleep(10)
        iframe = driver.find_element_by_xpath("//iframe[@id='iframepage']")
        driver.switch_to.frame(iframe)

        driver.find_element_by_xpath("//button[contains(text(),'查询')]").click()
        time.sleep(10)
        # driver.switch_to.parent_frame()
        driver.switch_to.default_content()
        driver.find_element_by_xpath("//a[contains(text(),'作业检查')]").click()
        time.sleep(3)

        driver.get_screenshot_as_file("d:\\1.png")
        time.sleep(3)
        self.quit(driver)
