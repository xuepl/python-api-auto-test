#! /usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from Common.baseui import baseUI


class Test_login():

    def test_login(self,driver):
        base = baseUI(driver)
        #打开网址
        driver.get("http://192.168.1.128:8090/#/login")
        #输入用户名//input[@name='username']
        base.send_keys('输入用户名',"//input[@name='username']",'admin')
        #输入密码//input[@name='password']
        base.send_keys('输入密码', "//input[@name='password']", '123456')
        #点击登录(//span[contains(text(),'登录')])[1]
        base.click("点击登录","(//span[contains(text(),'登录')])[1]")
        assert "首页" in driver.page_source
        #点击订单//span[@slot="title" and contains(text(),'订单')]
        base.click("点击订单","//span[@slot='title' and contains(text(),'订单')]")
        #点击订单列表(//span[contains(text(),'订单列表')])[1]
        base.click("点击订单列表","(//span[contains(text(),'订单列表')])[1]")
        #点击订单状态//label[contains(text(),'订单状态：')]/following-sibling::div//input
        base.click("点击订单状态","//label[contains(text(),'订单状态：')]/following-sibling::div//input")
        #选择待发货//span[contains(text(),'待发货')]
        base.click("选择待发货","//span[contains(text(),'待发货')]")
        #点击查询搜索//span[contains(text(),'查询搜索')]
        base.click("点击查询搜索","//span[contains(text(),'查询搜索')]")
        #选择第一条订单，点击订单发货//tbody/tr[1]/td[last()]//span[contains(text(),'订单发货')]
        base.click("选择第一条订单，点击订单发货","//tbody/tr[1]/td[last()]//span[contains(text(),'订单发货')]")
        #选择配送方式
        #点击请选择物流公司//tbody/tr[1]/td[last()-1]//input
        base.click("点击请选择物流公司","//tbody/tr[1]/td[last()-1]//input")

        #选择顺丰//span[contains(text(),'顺丰快递')]
        base.click("选择顺丰","//span[contains(text(),'顺丰快递')]")
        #输入物流单号//tbody/tr[1]/td[last()]//input
        base.send_keys("输入物流单号","//tbody/tr[1]/td[last()]//input","129031208391")
        #点击确定(//span[contains(text(),'确定')])[1]
        base.click("点击确定","(//span[contains(text(),'确定')])[1]")
        #点击确认提示(//span[contains(text(),'确定')])[2]
        base.click("点击确认提示","(//span[contains(text(),'确定')])[2]")
        #获取提示文本并断言 //div[@role='alert']/p
        actual = base.get_text("获取提示文本", "//div[@role='alert']/p")
        assert "发货成功" in actual

        sleep(2)