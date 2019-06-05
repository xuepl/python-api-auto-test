#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import requests

@pytest.fixture(scope="function")
def login():

    data ={"password": "123456","username": "admin"}

    r = requests.post(url="http://192.168.60.132:8080/admin/login",json=data)
    json = r.json()
    return json['data']["tokenHead"]+json['data']["token"]


def add_product_category(token):
    headers = {"Authorization":token}
    data={
  "description": "string",
  "icon": "string",
  "keywords": "string",
  "name": "string",
  "navStatus": 0,
  "parentId": 0,
  "productAttributeIdList": [
    0
  ],
  "productUnit": "string",
  "showStatus": 0,
  "sort": 0
}
    r = requests.post(url="http://192.168.60.132:8080/productCategory/create", json=data,headers = headers)
    print(r.text)
