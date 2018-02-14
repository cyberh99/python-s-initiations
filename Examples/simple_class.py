#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Simple_class:

    homer =  "ouch"

    def __init__(self, nombre):
        self.nombre = nombre
        print "Obiously it's a simple class"

    def say_hello(self):
        print "Hello %s"%(self.nombre)

    def say_goodbye(self):
        print "Goodbye %s"%(self.nombre)

    def flirt(self):
        self.say_hello()
        self.say_goodbye()
        print self.homer

objet = Simple_class("tito")
objet.flirt()

