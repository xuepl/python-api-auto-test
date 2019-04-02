#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time


def send_keys(driver,xpath,text):
    username = driver.find_element_by_xpath(xpath)
    # 清空
    username.clear()
    # 填值
    username.send_keys(text)
    time.sleep(2)