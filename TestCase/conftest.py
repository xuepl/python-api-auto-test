#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os

import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    driver_path = os.path.join(os.path.dirname(__file__), "../chromedriver/chromedriver.exe")
    # 打开浏览器
    driver = webdriver.Chrome(driver_path)
    driver.maximize_window()  # 最大化浏览器
    driver.implicitly_wait(8)  # 设置隐式时间等待
    yield driver
    driver.quit()
