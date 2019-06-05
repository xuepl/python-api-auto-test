#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


class TestDemo:
    @pytest.fixture(params=[[123, 234], [123, 234], [123, 234]])
    def b(self,request):
        return request.param


    @pytest.mark.huigui
    @pytest.mark.gongneng
    def test_b(self,b):
        print(b)

    @pytest.mark.huigui
    @pytest.mark.parametrize("a",[123,234,345])
    def test_abc(self,a):
        print(a)

    @pytest.mark.aaa
    def test_user_1(self,test_session,test_module,test_class,test_function):
        print('test_1')

    @pytest.mark.bbb
    def test_2(self,test_session,test_module,test_class,test_function):
        print('test_2')
    def test_22(self):
        a = ' adfsfsddddddfffghjkl; bz '
        print(a.replace(' ','s'))



    def test_de(self):
        stra='hello world'
