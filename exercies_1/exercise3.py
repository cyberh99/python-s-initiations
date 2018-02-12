#!/usr/bin/env pyhon
#-*- coding:utf-8 -*-

data = {}
print "Introduce nombre, edad y peso de los alumnos "
user_input = raw_input("Introduce los datos por teclado: ")

while user_input != "exit":
    try:
        user_data = user_input.split(";")
        data[user_data[0]] = [user_data[1],user_data[2]]
        user_input = raw_input("Introduce los datos por teclado: ")
    except Exception, e:
        print "ERROR: %s"%(e)
        sys.exit()

for alumno in data.keys():
    print "%s:%s"%(alumno,data[alumno])
