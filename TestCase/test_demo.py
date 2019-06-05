#! /usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep

import pyautogui
from pywinauto import Application

from TestCase.demo import *


class Test_demo():

    # def test_111(self):
    #     app = Application(backend="uia").start("‪C:\\Users\\xue00\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe")
    #     pyautogui.press("enter")
    #     pyautogui.press("f10")
    #     pyautogui.press("enter")
    #     #线程休眠2秒
    #     sleep(2)
    def test_222(self,login):
        add_product_category(login)