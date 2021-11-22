# -*- coding: utf-8 -*-
"""
Profesores: Gabriel Nuñez Y Luz Cardona
Integrantes:  David Mansilla, Elvis guerrero yRomina Muñoz
"""
#Comparar la cantidad de personas COVID positivos, pacientes en UCI y cantidad de examenes
#PCR en un dıa determinado, con el mismo dia del año anterior (si se tiene la informacion). Esta
#informacion sera para alguna region en particular y nivel paıs.


#-----------------------------------------------------------------------------#


#-----------------------------------------------------------------------------#
def regiones():
    print("0= arica y parinacota")
    print("1= tarapaca")
    print("2= Antofagasta")
    print("3= Atacama")
    print("4= Coquimbo")
    print("5= Valparaiso")
    print("6= Metropolitana")
    print("7= O’Higgins")
    print("8= Maule")
    print("9= Ñuble")
    print("10= Biobío")
    print("11= Araucanía")
    print("12= Los Ríos")
    print("13= Los Lagos")
    print("14= Aysén")
    print("15= Magallanes")
    
def menu():
    print("\n\n\t ---MENU--- \n")
    print("Bienvenido usuario, porfavor ingrese la opcion que desea utilizar")
    print("Opcion 1: Mostrar la cantidad de personas con Covid positivo. ")
    print("Opcion 2: Mostrar pacientes ingresados en UCI (pacientes con cuidados intensivos). ")
    print("Opcion 3: Mostrar cantidad de examenes PCR por dia especifico, region especifica o nivel país.")
    print("Opcion 0: Cerrar el programa")
    respuesta= int(input("Ingrese su opcion: "))
    return respuesta

def casosN(lineas):
    
    region = []
    fechas = lineas[0].split(',')
    
    i = 1
    while (i < len(lineas)):
        lineanueva = lineas[i].split(',')
        j = 1
        personascovid = {}
        while(j<len(lineanueva)):
            personascovid[fechas[j]]=lineanueva[j]
            j = j + 1
        region.append(personascovid)
        i = i + 1
        
    return region

def casosPorRegion():
    casos = open("Casos-nuevos-totales-por-region.txt" , "r")
    leido = casos.readlines()   
    personascovid = casosN(leido)
    x=int(input("ingrese el valor de la region que quiera ver: "))
    y=input("Ingrese la fecha que le gustaria revisar, con el formato de año, mes y dia separados por un -, ejemplo: 2020-03-04")
    print(personascovid[x][y])
    casos.close()  
    return
def examenesP(lineaS):
        
    regionE = []
    fechasE = lineaS[0].split(',')
    
    i = 1
    while(i < len(lineaS)):
        lineaSnueva = lineaS[1].split(',')
        j = 3 
        examenesScovid = {}
        while(j<len(lineaSnueva)):
            examenesScovid[fechasE[j]] = lineaSnueva[j]
            j = j + 1
        regionE.append(examenesScovid)
        i = i + 1
    return regionE

def ExamenesPCR():
    examenes = open("Examenes-PCR-region.txt", "r")
    leidoS = examenes.readlines()
    examenesScovid = examenesP(leidoS)
    x=int(input("ingrese el valor de la region que quiera ver: "))
    y=input("Ingrese la fecha que le gustaria revisar, con el formato de año, mes y dia separados por un -, ejemplo: 2020-03-04")
    print(examenesScovid[x][y])
    examenes.close()
    return

def pacientesU(lineasU):
    
    regionU = []
    fechasU = lineasU[0].split(',')
    
    i = 1
    while(i < len(lineasU)):
        lineaUnueva = lineasU[1].split(',')
        j = 3
        pacienteUcovid = {}
        while(j < len(lineaUnueva)):
            pacienteUcovid[fechasU[j]] = lineaUnueva[j]
            j = j + 1
        regionU.append(pacienteUcovid)
        i = i + 1
    return regionU

def PacientesUCI():
    pacientesUCI = open("Pacientes-UCI-region.txt" , "r")
    leidoU = pacientesUCI.readlines()
    pacienteUcovid = pacientesU(leidoU)
    x=int(input("ingrese el valor de la region que quiera ver: "))
    y=input("Ingrese la fecha que le gustaria revisar, con el formato de año, mes y dia separados por un -, ejemplo: 2020-03-04")
    print(pacienteUcovid[x][y])
    pacientesUCI.close()

respuesta=menu()

if respuesta==0:
    print("el programa se cerro")









