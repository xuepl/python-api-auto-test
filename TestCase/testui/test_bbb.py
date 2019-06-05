#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from Common.baseui import baseUI


class TestDemo:
    @pytest.mark.aaa
    def test_3(self,test_session,test_module,test_class,test_function):
        print('test_3')

    @pytest.mark.bbb
    def test_4(self,test_session,test_module,test_class,test_function):
        print('test_4')

    def test_ui(self,driver):
        base = baseUI(driver)

        base.click_by_js('点击按钮','xpath')
