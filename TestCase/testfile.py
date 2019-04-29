#! /usr/bin/env python
# -*- coding: utf-8 -*-
import random


for i in range(1,1000):
    for j in range(i, 1000):
        for k in range(j, 1000):
            if (k*k == i * i + j * j):
                print("{0},{1},{2}".format(i,j,k))
