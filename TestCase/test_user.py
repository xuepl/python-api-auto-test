#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import requests
from allure_commons._allure import title

from Common.Assert import Assertion
from Common.Request import Request, allure


class TestUser():

    def test_register(self,data):
        request = Request()
        r = request.get_request(data[3])
        Assertion.assert_in_text(r.text,"200")


