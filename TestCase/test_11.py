#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import requests

from Common.conf import HOST
from Common.read_excel import read_excel_list


class Tesat002():

    @pytest.mark.parametrize("email,icon,nickName,note,password,username,ass",read_excel_list("E:\\ceshi.xls"))
    def test_register(self,email,icon,nickName,note,password,username,ass):
        data = {  "email": email,  "icon": icon,  "nickName": nickName,  "note": note,  "password": password,  "username": username}
        r = requests.post(url=HOST + "/admin/register", json=data)
        print(r.text)
        assert ass in r.text


