#! /usr/bin/env python
# -*- coding: utf-8 -*-
import allure
from selenium import webdriver
import time
import os

from Common.baseui import *

from Common.Assert import Assertion


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

        #打开网址
        driver.get("http://192.168.60.132/#/login")
        #输入用户名//input[@name='username']
        send_keys(driver,"//input[@name='username']","admin")
        #输入密码//input[@name='password']
        send_keys(driver, "//input[@name='password']", "123456")
        #点击登录(//span[contains(text(),'登录')])[1]
        login_button = driver.find_element_by_xpath("(//span[contains(text(),'登录')])[1]")
        login_button.click()
        time.sleep(2)
        #点击商品(//span[contains(text(),'商品')])[1]
        sp_button = driver.find_element_by_xpath("(//span[contains(text(),'商品')])[1]")
        sp_button.click()
        time.sleep(2)
        #点击添加商品//span[contains(text(),'添加商品')]
        addsp_button = driver.find_element_by_xpath("//span[contains(text(),'添加商品')]")
        addsp_button.click()
        time.sleep(2)
        #点击商品分类//label[contains(text(),'商品分类：')]/following-sibling::div/span
        spfl_button = driver.find_element_by_xpath("//label[contains(text(),'商品分类：')]/following-sibling::div/span")
        spfl_button.click()
        time.sleep(2)
        #点击汽车用品//li[contains(text(),'汽车用品')]
        driver.find_element_by_xpath("//li[contains(text(),'汽车用品')]").click()
        time.sleep(2)
        #点击全新整车//li[contains(text(),'全新整车')]
        driver.find_element_by_xpath("//li[contains(text(),'全新整车')]").click()
        time.sleep(2)
        #输入商品名称//label[contains(text(),'商品名称：')]/following-sibling::div//input
        sp_name = driver.find_element_by_xpath("//label[contains(text(),'商品名称：')]/following-sibling::div//input")
        # 清空
        sp_name.clear()
        # 填值
        sp_name.send_keys("凯迪拉克")
        #输入副标题//label[contains(text(),'副标题：')]/following-sibling::div//input
        f_title = driver.find_element_by_xpath("//label[contains(text(),'副标题：')]/following-sibling::div//input")
        # 清空
        f_title.clear()
        # 填值
        f_title.send_keys("astl")
        #点击商品品牌//label[contains(text(),'商品品牌：')]/following-sibling::div/div
        driver.find_element_by_xpath("//label[contains(text(),'商品品牌：')]/following-sibling::div/div").click()
        time.sleep(2)
        #点击小米//span[text()='小米']
        driver.find_element_by_xpath("//span[text()='小米']").click()
        time.sleep(2)
        #输入商品介绍//label[contains(text(),'商品介绍')]/following-sibling::div//textarea
        spjs = driver.find_element_by_xpath("//label[contains(text(),'商品介绍')]/following-sibling::div//textarea")
        # 清空
        spjs.clear()
        # 填值
        spjs.send_keys("sadfasdf")
        #输入商品货号//label[contains(text(),'商品货号')]/following-sibling::div//input
        sphh = driver.find_element_by_xpath("//label[contains(text(),'商品货号')]/following-sibling::div//input")
        # 清空
        sphh.clear()
        # 填值
        sphh.send_keys("12345677890")
        #输入商品售价//label[contains(text(),'商品售价')]/following-sibling::div//input
        spsj = driver.find_element_by_xpath("//label[contains(text(),'商品售价')]/following-sibling::div//input")
        # 清空
        spsj.clear()
        # 填值
        spsj.send_keys("9.9")
        #输入市场价//label[contains(text(),'市场价')]/following-sibling::div//input
        scj = driver.find_element_by_xpath("//label[contains(text(),'市场价')]/following-sibling::div//input")
        # 清空
        scj.clear()
        # 填值
        scj.send_keys("99")
        #输入商品库存
        #输入计量单位
        #下拉窗口
        js = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js)
        time.sleep(2)
        #输入商品重量
        #输入排序
        #点击下一步//span[text()='下一步，填写商品促销']
        driver.find_element_by_xpath("//span[text()='下一步，填写商品促销']").click()
        #allure.attach(driver.get_screenshot_as_png(),'测试一下',allure.attachment_type.PNG)
        time.sleep(2)
        #下一步，填写商品属性
        driver.find_element_by_xpath("//span[text()='下一步，填写商品属性']").click()
        time.sleep(2)

        driver.switch_to.frame(driver.find_element_by_xpath("(//iframe[contains(@id,'vue-tinymce-')])[1]"))
        time.sleep(2)
        driver.find_element_by_id("tinymce").send_keys('ceshiyixia')
        time.sleep(2)
