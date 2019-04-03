#! /usr/bin/env python
# -*- coding: utf-8 -*-
import allure
from selenium import webdriver
import time
import os

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from Common.Assert import Assertion
from Common.baseui import baseUI


class TestFirstUIDemo:

    def tttttest_demo1(self,driver):
        time.sleep(2)
        #打开网址
        driver.get("http://192.168.60.132/#/login")
        #输入用户名
        #通过xpath定位元素
        username = driver.find_element_by_xpath("//input[@name='username']")
        username.clear()
        username.send_keys("admin")
        time.sleep(2)
        #数据密码
        password = driver.find_element_by_xpath('//input[@name="password"]')
        password.clear()
        password.send_keys("123456")
        time.sleep(2)
        #点击登录
        login = driver.find_element_by_xpath("(//span[contains(text(),'登录')])[1]")
        login.click()
        time.sleep(2)

        #断言

        Assertion.assert_in_text(driver.page_source,'首页')



        #点击营销
        yingxiao = driver.find_element_by_xpath("//span[contains(text(),'营销')]")
        yingxiao.click()
        time.sleep(2)

        #点击优惠券列表
        youhuiquanliebiao = driver.find_element_by_xpath("//span[contains(text(),'优惠券列表')]")
        youhuiquanliebiao.click()
        time.sleep(2)
        #输入优惠券名称
        youhuiquanmingcheng = driver.find_element_by_xpath("//input[@placeholder='优惠券名称']")
        youhuiquanmingcheng.clear()
        youhuiquanmingcheng.send_keys("小米手机专用券")
        time.sleep(2)
        #点击查询搜索
        chaxunsousuo  = driver.find_element_by_xpath('//span[contains(text(),"查询搜索")]')
        chaxunsousuo.click()
        time.sleep(2)

    def test_demo2(self,driver):
        base = baseUI(driver)

        #打开网址
        driver.get("http://192.168.60.132/#/login")
        #输入用户名//input[@name='username']
        base.send_keys("输入用户名","//input[@name='username']","admin")
        #输入密码//input[@name='password']
        base.send_keys("输入密码","//input[@name='password']", "123456")
        #点击登录(//span[contains(text(),'登录')])[1]
        base.click('点击登录',"(//span[contains(text(),'登录')])[1]")
        base.click('点击商品',"//span[text()='商品']")
        #点击添加商品
        base.click("点击添加商品","//span[text()='添加商品']")
        #点击商品分类
        base.click("点击商品分类","//label[contains(text(),'商品分类')]/following-sibling::div/span")
        #点击服装
        base.click("点击服装","//li[contains(text(),'服装')]")
        #点击外套
        base.click("点击外套","//li[contains(text(),'外套')]")
        #填写商品名称
        base.send_keys("填写商品名称","//label[contains(text(),'商品名称')]/following-sibling::div//input","缺了个口子")
        #填写副标题
        base.send_keys("填写副标题","//label[contains(text(),'副标题')]/following-sibling::div//input","谁啃得")
        #点击商品品牌
        base.click("点击商品品牌","//label[contains(text(),'商品品牌')]/following-sibling::div/div")
        #点击苹果
        base.click("点击苹果","//span[text()='苹果']")
        #滚动窗口
        base.scroll_screen("滚动窗口")
        #点击下一步
        base.click("击下一步","//span[text()='下一步，填写商品促销']")
        #点击下一步
        base.click("点击下一步","//span[text()='下一步，填写商品属性']")
        #上传商品图片
        #base.send_keys("上传商品图片","//input[@name='file']/parent::*","‪D:\\1.png")
        #切换iframe
        base.switch_to_frame("切换到iframe","(//iframe[contains(@id,'vue-tinymce-')])[1]")
        #填写规格参数
        base.send_keys("填写规格参数","//body[@id='tinymce']","测试一下")
        driver.switch_to.default_content()
        #点击下一步
        base.click("点击下一步","//span[contains(text(),'下一步，选择商品关联')]")
        #点击完成商品
        base.click("点击完成商品","//span[contains(text(),'完成，提交商品')]")
        #切换到弹框
        base.click("点击弹框","//span[contains(text(),'确定')]/parent::*")
        time.sleep(1)

        time.sleep(5)


    def test_demo3(self,driver):
        base = baseUI(driver)
        driver.get("file:///E:/softwaredata/01_%E6%95%99%E5%AD%A6/1902%E5%88%9D%E7%BA%A7%E7%8F%AD/demo.html")
        #base.send_keys("上传文件","//input[@type='file']","‪D:/1.png")
        #删除日期控件，只读属性
        #base.remove_attribute_by_xpath("删除日期控件，只读属性","//input[@type='date']","readonly")
        # base.update_attribute_by_xpath("修改日期控件value值","//input[@type='date']",'value','2019-04-03')
        # base.select_by_visible_text("选择丁雁玲","//select","丁雁玲")
        # time.sleep(1)
        # base.select_by_value("选择魏谦","//select","w")
        # time.sleep(1)
        # base.select_by_index("选择丁雁玲","//select",1)
        # select = Select(driver.find_element_by_xpath("//select"))
        # select.select_by_visible_text("丁雁玲")
        # time.sleep(1)
        # select.select_by_index(2)
        # time.sleep(1)
        # select.select_by_value("d")
        #base.click("点击百度","//a[contains(text(),'百度')]")
        action = ActionChains(driver)
        action.key_down(Keys.CONTROL).click(driver.find_element_by_xpath("//a[contains(text(),'百度')]")).key_up(Keys.CONTROL).perform()
        time.sleep(3)
        action.key_down(Keys.SHIFT).click(driver.find_element_by_xpath("//a[contains(text(),'百度')]")).key_up(Keys.SHIFT).perform()
        time.sleep(5)

    def test_demo4(self,driver):
        base = baseUI(driver)
        # 打开网址
        driver.get("http://192.168.60.132/#/login")
        # 输入用户名//input[@name='username']
        base.send_keys("输入用户名", "//input[@name='username']", "admin")
        # 输入密码//input[@name='password']
        base.send_keys("输入密码", "//input[@name='password']", "123456")
        # 点击登录(//span[contains(text(),'登录')])[1]
        base.click('点击登录', "(//span[contains(text(),'登录')])[1]")
        #点击营销
        base.click("点击营销","//span[text()='营销']")
        #点击优惠券列表(//span[contains(text(),'优惠券列表')])[1]
        base.click("点击优惠券列表","(//span[contains(text(),'优惠券列表')])[1]")
        #点击第一条数据的编辑(//tr)[2]//span[contains(text(),'编辑')]
        base.click("点击第一条数据的编辑","(//tr)[2]//span[contains(text(),'编辑')]")
        #点击提交//span[contains(text(),'提交')]
        base.click("点击提交","//span[contains(text(),'提交')]")
        #点击确定//span[contains(text(),'确定')]
        base.click("点击确定","//span[contains(text(),'确定')]")
        print(driver.page_source)
        text = base.get_text("获取页面展示文本","//div[@role='alert']/p")
        print(driver.page_source)
        #print(text)
        time.sleep(4)









