#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Animal:
    def __init__(self):
    
        print "It's an animal"

    def born(self):
        print "It's borning a new animal"

    def breathe(self):
        print "It's breathing"

class dog(Animal):
    def new_dog(self):
        self.born()
        self.breathe()

c = dog()

c.new_dog()
