#!/usr/bin/env python
#-*- coding: utf-8 -*-


class super_calculator:
    def __init__(self,num1,num2):
        print "It's too simple"
        self.num1 = num1
        self.num2 = num2

    def __mult(self):
               
        f_number = self.num1 * self.num2
        return f_number

    def operate(self):
        print self.__mult()
        

casio = super_calculator(2,2)
casio.operate()

