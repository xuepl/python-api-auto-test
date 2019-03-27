#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

l=[["订单管理","订单查询","根据订单号查询",'http://192.168.60.132:8080/order/12']]

def id(fixture_value):
    return "测试用例名：%s"%(fixture_value[2])

@pytest.fixture(params=l,ids=id)
def data(request):
    return request.param