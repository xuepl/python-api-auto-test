#! /usr/bin/env python
# -*- coding: utf-8 -*-

def fun1(function):
    def func():
        print("log之前")
        function()
        print("log之后")

    return func

@fun1
def log():
    print("log")


def fun(function):
    def wap():
        print("wap")
        function()
    return wap



if __name__ == '__main__':
    log()

