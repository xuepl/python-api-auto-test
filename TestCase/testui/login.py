#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time

from Common.baseui import baseUI


def login(driver):
    base = baseUI(driver)

    # 打开网址
    driver.get("http://192.168.1.137/#/login")
    # 定位并处理异常弹框//span[contains(text(),'残忍拒绝')]

    # 定位用户名输入框//input[@name='username']
    # username = driver.find_element_by_xpath("//input[@name='username']")
    # 输入用户名
    # username.clear()
    # username.send_keys("admin")
    # 定位密码输入框//input[@name='password']
    # password = driver.find_element_by_xpath("//input[@name='password']")
    # 输入密码
    # password.clear()
    # password.send_keys("123456")
    # 定位登录按钮(//span[contains(text(),'登录')])[1]
    base.click("点击登录按钮", "(//span[contains(text(),'登录')])[1]")
    # 点击登录按钮

    try:
        base.click("点击残忍拒绝", "//span[contains(text(),'残忍拒绝')]")
    except:
        pass
    # 线程等待，特定程序执行到该语句就会休眠给定的时间，时间到，继续执行下边的代码。写代码调试的时候用
    time.sleep(2)
    # selenium提供了一个显示等待，特点：判断页面元素是否达到某种状态，如果条件满足程序就会往下执行，如果不满足，超时时间达到，就会抛出异常，代码会终止
    # WebDriverWait(driver, 5, 0.3).until(EC.presence_of_element_located((By.XPATH, "(//span[contains(text(),'登录')])[1]"))).click()
    base.click("点击登录按钮", "(//span[contains(text(),'登录')])[1]")
    time.sleep(1)
    # 断言页面是否跳转到首页
    assert "首页" in driver.page_source