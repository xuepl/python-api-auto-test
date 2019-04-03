#! /usr/bin/env python
# -*- coding: utf-8 -*-
import allure
from selenium import webdriver
import time
import os



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
        time.sleep(2)


