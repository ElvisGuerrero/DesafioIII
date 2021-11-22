# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 12:46:52 2021

@author: Romina Muñoz, Elvis guerrero, David Mansilla
"""
#Mostrar por pantalla la cantidad de personas COVID positivos, pacientes en UCI y cantidad de
#ex´amenes PCR en un d´ıa determinado para alguna regi´on en particular y nivel pa´ıs.


casos = open("Casos-nuevos-totales-por-region.txt")
examenes = open("Examenes-PCR-region.txt")
pacientes = open("Pacientes.UCI-region.txt")
#-----------------------------------------------------------------------------#
casos.readlines()
examenes.readlines()
pacientes.readlines()

#-----------------------------------------------------------------------------#

def menu():
    print("\n\n\t ---MENU--- \n")
    print("Bienvenido usuario, porfavor ingrese la opcion que desea utilizar")
    print("Opcion 1: Mostrar la cantidad de personas con Covid positivo. ")
    print("Opcion 2: Mostrar pacientes ingresados en UCI (pacientes con cuidados intensivos). ")
    print("Opcion 3: Mostrar cantidad de examenes PCR por dia especifico, region especifica o nivel país.")
    


    
