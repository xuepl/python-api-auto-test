#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By



def shot(func):
    def function(*args, **kwargs):
        allure.attach(args[0].driver.get_screenshot_as_png(), args[1] + '之前', allure.attachment_type.PNG)

        func(*args, **kwargs)
        allure.attach(args[0].driver.get_screenshot_as_png(), args[1] + '之后', allure.attachment_type.PNG)

    return function


class baseUI():

    def __init__(self,driver):
        self.driver = driver

    def local_element(self,xpath):
       return WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located((By.XPATH,xpath)))

    @shot
    def send_keys(self,step,xpath,text):
        '''
        文本输入框清空并填值
        :param step:操作步骤
        :param xpath: xpath
        :param text: 填的值
        :return:
        '''
        element = self.local_element(xpath)
        element.clear()
        element.send_keys(text)


    @shot
    def click(self,step,xpath):
        '''
        #点击操作
        :param step: 操作步骤
        :param xpath: xpath
        :return:
        '''
        element = self.local_element(xpath)
        element.click()
    @shot
    def scroll_screen(self,step):
        '''
        #滚动窗口
        :param step:操作步骤
        :return:
        '''
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
    @shot
    def switch_to_frame(self,step,xpath):
        '''
        #切换到iframe里边
        :param step:操作步骤
        :param xpath: xpath
        :return:
        '''
        element = self.local_element(xpath)
        self.driver.switch_to.frame(element)
    def switch_to_content(self,step):
        '''
        #切出iframe，回到默认页面
        :param step:操作步骤
        :return:
        '''