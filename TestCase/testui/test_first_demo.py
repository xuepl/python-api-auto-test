#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time

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
        radio = driver.find_element_by_xpath("//td[contains(text(),'radio:单选框')]/following-sibling::td//input[2]")
        #点击
        radio.click()


        #定位第一个多选框//td[contains(text(),'checkbox:多选框')]/following-sibling::td//input[1]
        checkbox = driver.find_element_by_xpath("//td[contains(text(),'checkbox:多选框')]/following-sibling::td//input[1]")
        #点击
        checkbox.click()
        time.sleep(2)
        checkbox.click()
        print(type(checkbox))
        time.sleep(2)
        #全选//td[contains(text(),'checkbox:多选框')]/following-sibling::td//input
        checkboxes = driver.find_elements_by_xpath("//td[contains(text(),'checkbox:多选框')]/following-sibling::td//input")
        for c in checkboxes:
            c.click()
        time.sleep(2)
        self.quit(driver)
