#!/usr/bin/env python
#-*- coding:utf-8 -*-

user_input = raw_input("Introduce algo por teclado: ")
data = []
while user_input != "exit":
    data.append(user_input)
    user_input = raw_input("Introduce algo por teclado: ")

for element in data:
    print element
