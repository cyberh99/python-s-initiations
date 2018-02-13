#!/usr/bin/nev python
#-*- coding: utf-8 -*-
alumnos={}

final_register={}


def agregar_alumno(nombre,altura,peso):
    alumnos[nombre] = [altura,peso]

def calcular_indice(altura,peso):
    indice = float(peso) / (float(altura) * float(altura))

    return indice

entrada = raw_input(":> ")

while entrada != "exit":
    data = entrada.split(" ")
    agregar_alumno(data[0],data[1],data[2])
    entrada = raw_input(":> ")


for alumno in alumnos.keys():

    indice_alumno = calcular_indice(alumnos[alumno][0] ,alumnos[alumno][1])
    final_register.update({alumno:indice_alumno})

print final_register
'''

for alumno in alumnos.keys():
    print calcular_indice( alumnos[alumno][0], alumnos[alumno][1])'''
