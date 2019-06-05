#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os

import pytest
import requests
from selenium import webdriver




@pytest.fixture(scope="session")
def driver():
    driver_path = os.path.join(os.path.dirname(__file__), "../chromedriver/chromedriver.exe")
    # 打开浏览器
    dr = webdriver.Chrome(driver_path)
    dr.maximize_window()  # 最大化浏览器
    dr.implicitly_wait(8)  # 设置隐式时间等待

    yield dr
    dr.quit()


@pytest.fixture(scope="session")
def token():
    data = {
        "password": "123456",
        "username": "admin"
    }
    r = requests.post(url='http://192.168.60.132:8080/admin/login', json=data)
    r_json = r.json()
    print(r_json)
    assert 200 == r_json["code"]
    global token
    return {"Authorization":r_json["data"]['tokenHead'] + r_json["data"]['token']}


@pytest.fixture(scope="session")
def test_session():
    print('------------------session之前---------------------------')
    yield
    print('------------------session之后---------------------------')

@pytest.fixture(scope="module")
def test_module():
    print('------------------module之前---------------------------')
    yield
    print('------------------module之后---------------------------')
@pytest.fixture(scope="class")
def test_class():
    print('------------------class之前---------------------------')
    yield
    print('------------------class之后---------------------------')

@pytest.fixture(scope="function")
def test_function():
    print('------------------function之前---------------------------')
    yield
    print('------------------function之后---------------------------')
