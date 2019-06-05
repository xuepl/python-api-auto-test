#! /usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

import pyperclip
import pyautogui



def test_111(driver):
    screenWidth, screenHeight = pyautogui.size()
    pyautogui.moveTo(1900, 50)
    pyautogui.click()
    sleep(10)
