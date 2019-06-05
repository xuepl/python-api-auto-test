#! /usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

import pyautogui
import pytest
import requests

from tools.mysql_tools import mysql_db


class Test001():

    def test_111(self,driver):
        pyautogui.press("enter")
        pyautogui.press("f10")
        pyautogui.press("enter")
        sleep(10)


    # @pytest.mark.parametrize("amount",[1,2,3,4,5,6])
#     def test_02(self,token,amount):
#         data = {
#   "amount": amount,
#   "code": "string",
#   "count": 0,
#   "enableTime": "2019-05-19T06:15:10.018Z",
#   "endTime": "2019-05-19T06:15:10.018Z",
#   "id": 0,
#   "memberLevel": 0,
#   "minPoint": 0,
#   "name": "string",
#   "note": "string",
#   "perLimit": 0,
#   "platform": 0,
#   "productCategoryRelationList": [
#     {
#       "couponId": 0,
#       "id": 0,
#       "parentCategoryName": "string",
#       "productCategoryId": 0,
#       "productCategoryName": "string"
#     }
#   ],
#   "productRelationList": [
#     {
#       "couponId": 0,
#       "id": 0,
#       "productId": 0,
#       "productName": "string",
#       "productSn": "string"
#     }
#   ],
#   "publishCount": 0,
#   "receiveCount": 0,
#   "startTime": "2019-05-19T06:15:10.018Z",
#   "type": 0,
#   "useCount": 0,
#   "useType": 0
# }
#
#         r = requests.post(url='http://192.168.60.132:8080/coupon/create', json=data,headers = token)
#         print(r.text)
#
#     @pytest.fixture(scope="function")
#     def order_id(self,token):
#         db = mysql_db("192.168.60.132", 'root', 'root', 'mall')
#         order_sn = db.select_execute("SELECT order_sn FROM oms_order WHERE STATUS=1 AND delete_status=0;")
#         data = {'orderSn':order_sn[0],'receiverKeyword':"",'status':1,'orderType':None,'sourceType':None,'createTime':"",'pageSize':5,'pageNum':1}
#         r = requests.get(url='http://192.168.60.132:8080/order/list', params=data, headers=token)
#         print(r.text)
#         return r.json()["data"]["list"][0]["id"]
#
#     def test_fahuo(self,token,order_id):
#         data = [
#   {
#     "deliveryCompany": "string",
#     "deliverySn": "string",
#     "orderId": order_id
#   }
# ]
#         r = requests.post(url='http://192.168.60.132:8080/order/update/delivery', json=data, headers=token)
#         print(r.text)









