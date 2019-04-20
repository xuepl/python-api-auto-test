#! /usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest
from selenium import webdriver
import time
import os

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
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

    def tes333t_demo2(self,driver):
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

    @pytest.mark.windows
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
        action.key_down(Keys.CONTROL).click(driver.find_element_by_xpath("//a[contains(text(),'京东')]")).key_up(
            Keys.CONTROL).perform()
        action.key_down(Keys.CONTROL).click(driver.find_element_by_xpath("//a[contains(text(),'当当')]")).key_up(
            Keys.CONTROL).perform()
        base.switch_to_windows_by_title('切换窗口至京东','京东')
        time.sleep(3)
        # action.key_down(Keys.SHIFT).click(driver.find_element_by_xpath("//a[contains(text(),'百度')]")).key_up(Keys.SHIFT).perform()
        time.sleep(5)
        driver.switch_to.window()

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
        text = base.get_text("获取页面展示文本","//div[@role='alert']")
        #print(driver.page_source)
        #
        #print(text)
        Assertion.assert_in_text(text,'修改成功')

    def test_demo5(self,driver):
        base = baseUI(driver)
        # 打开网址
        # driver.get("http://192.168.60.132/#/login")
        # # 输入用户名//input[@name='username']
        # base.send_keys("输入用户名", "//input[@name='username']", "admin")
        # # 输入密码//input[@name='password']
        # base.send_keys("输入密码", "//input[@name='password']", "123456")
        # # 点击登录(//span[contains(text(),'登录')])[1]
        # base.click('点击登录', "(//span[contains(text(),'登录')])[1]")
        #点击订单//span[text()='订单']
        base.click("点击订单","//span[text()='订单']")
        #点击订单列表(//span[text()='订单列表'])[1]
        base.click("点击订单列表", "(//span[text()='订单列表'])[1]")
        #点击订单状态//label[contains(text(),'订单状态：')]/following-sibling::div//input
        base.click("点击订单状态", "//label[contains(text(),'订单状态：')]/following-sibling::div//input")
        #点击待发货//span[text()='待发货']
        base.click("点击待发货", "//span[text()='待发货']")
        #点击搜索查询//span[contains(text(),'查询搜索')]
        base.click("点击搜索查询", "//span[contains(text(),'查询搜索')]")
        #记录第一条的编号//tbody/tr[1]/td[2]/div
        num = base.get_text('获取编号',"//tbody/tr[1]/td[2]/div")
        order_num = base.get_text("获取订单编号","//tbody/tr[1]/td[3]/div")
        #点击第一条订单发货//tbody/tr[1]/td[10]/div/button[3]
        base.click("点击第一条订单发货","//tbody/tr[1]/td[10]/div/button[3]")
        #点击配送方式//input[@placeholder='请选择物流公司']
        base.click("点击配送方式","//input[@placeholder='请选择物流公司']")
        #点击圆通快递//span[text()='圆通快递']
        base.click("点击圆通快递","//span[text()='圆通快递']")
        #输入物流单号//tbody/tr/td[7]//input
        base.send_keys("输入物流单号","//tbody/tr/td[7]//input","123456789")
        #点击确定//span[text()='确定']
        base.click("点击确定","//span[text()='确定']")
        #确认(//span[contains(text(),'确定')])[2]
        base.click("确认","(//span[contains(text(),'确定')])[2]")
        #获取提示框文本//div[@role='alert']/p
        text = base.get_text("获取提示框文本","//div[@role='alert']/p")
        #断言
        Assertion.assert_in_text(text,'发货成功')
        # 点击订单状态//label[contains(text(),'订单状态：')]/following-sibling::div//input
        base.click("点击订单状态", "//label[contains(text(),'订单状态：')]/following-sibling::div//input")
        # 点击已发货//span[text()='待发货']
        base.click("点击已发货", "//span[text()='已发货']")
        #输入订单编号//input[@placeholder='订单编号']
        base.send_keys("输入订单编号","//input[@placeholder='订单编号']",order_num)
        # 点击搜索查询//span[contains(text(),'查询搜索')]
        base.click("点击搜索查询", "//span[contains(text(),'查询搜索')]")
        #定位到刚才发货的订单
        time.sleep(1)
        #通过xpath定位到一组元素，存到一个list中
        nums = driver.find_elements_by_xpath("(//tbody)[1]/tr/td[2]")
        #存放是否能找到编号 找到true  未找到 false
        b = False
        #遍历上边的list
        for n in nums:
            #n.text取出元素的可视文本
            print(n.text)
            #判断可视文本是否与发货订单的编号相同
            if n.text == num:
                #如果相同，就讲true赋值给b
                b = True
        #断言，订单状态转换是否正确
        assert True == b
        time.sleep(3)
    def test_demo6(self, driver):
        base = baseUI(driver)
        # 打开网址
        driver.get("http://192.168.60.132/#/login")
        # 输入用户名//input[@name='username']
        base.send_keys("输入用户名", "//input[@name='username']", "admin")
        # 输入密码//input[@name='password']
        base.send_keys("输入密码", "//input[@name='password']", "123456")
        # 点击登录(//span[contains(text(),'登录')])[1]
        base.click('点击登录', "(//span[contains(text(),'登录')])[1]")
        # 点击订单//span[text()='订单']
        base.click("点击订单", "//span[text()='订单']")
        # 点击订单列表(//span[text()='订单列表'])[1]
        base.click("点击订单列表", "(//span[text()='订单列表'])[1]")
        # 点击订单状态//label[contains(text(),'订单状态：')]/following-sibling::div//input
        base.click("点击订单状态", "//label[contains(text(),'订单状态：')]/following-sibling::div//input")
        # 点击待发货//span[text()='待发货']
        base.click("点击待发货", "//span[text()='待发货']")
        # 点击搜索查询//span[contains(text(),'查询搜索')]
        base.click("点击搜索查询", "//span[contains(text(),'查询搜索')]")
        #点击全选(//label[@role='checkbox'])[1]
        base.click("点击全选","(//label[@role='checkbox'])[1]")
        #滚动窗口到最后
        base.scroll_screen('滚动屏幕')
        #点击批量操作//input[@placeholder='批量操作']
        base.click("点击批量操作","//input[@placeholder='批量操作']")
        #选择批量发货//span[text()='批量发货']
        base.click("选择批量发货","//span[text()='批量发货']")
        #点击确定//span[contains(text(),'确定')]
        base.click("点击确定","//span[contains(text(),'确定')]")
        #获取总共有多少行
        rows = len(driver.find_elements_by_xpath("//tbody/tr"))
        #选择物流公司//tbody/tr[1]/td[6]//input
        #选择快递(//span[text()='中通快递'])[1]
        #物流单号//tbody/tr[1]/td[7]//input

        for i in range(1,rows+1):
            # 选择物流公司//tbody/tr[1]/td[6]//input
            base.click("点击选择物流公司","//tbody/tr[{0}]/td[6]//input".format(i))
            # 选择快递(//span[text()='中通快递'])[1]
            base.click("选择快递","(//span[text()='中通快递'])[10]")
            #物流单号//tbody/tr[1]/td[7]//input
            base.send_keys("填写物流单号","//tbody/tr[{0}]/td[7]//input".format(i),"265688456486")
        time.sleep(2)
        driver.find_element_by_xpath().get_attribute("class")

        pass






