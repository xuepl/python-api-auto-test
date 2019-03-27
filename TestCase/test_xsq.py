#! /usr/bin/env python
# -*- coding: utf-8 -*-



def logs(xpath):
    def swap(func):
        def _func(*args, **kwargs):
            print(xpath)
            print("定位操作")
            return func(*args, **kwargs)

        return _func
    return swap





@logs(xpath="111111")
def test_local():
    print("操作函数")


def test_host():
    print("1111")

