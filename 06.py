# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:05:24 2019

@author: ki10m
"""
num =10

while num>0:
    a = int(input('please input<'))
    if a%7==0:
        print('7の倍数です')
    if a%3==0:
        print('3の倍数です')
    if a<0:
        print('負数です')
    num-=1
