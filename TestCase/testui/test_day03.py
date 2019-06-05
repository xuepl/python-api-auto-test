#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Common.baseui import baseUI
from Common.read_excel import *
from TestCase.testui.login import login


class TestMall():

    @pytest.mark.s
    def tes1t_login(self,driver):
        login(driver)

    def test_order_1(self,driver):

        print("查询订单")

        pass

    l_name = read_excel_list("d:\\data.xlsx")

    @pytest.fixture(params=l_name)
    def name(self,request):
        return request.param

    def test_order_2(self,name):
        print(name[0])

        pass
