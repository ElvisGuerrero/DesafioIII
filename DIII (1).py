# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 12:46:52 2021

@author: Romina Muñoz, Elvis guerrero, David Mansilla
"""
#Comparar la cantidad de personas COVID positivos, pacientes en UCI y cantidad de ex´amenes
#PCR en un d´ıa determinado, con el mismo dia del año anterior (si se tiene la informaci´on). Esta
#informaci´on ser´a para alguna regi´on en particular y nivel pa´ıs.




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
    print("Opcion 3: Mostrar la tasa de positividad de un día especifico.")
    print("Opcion 4: Comparar fechas con el año anterior.")
    print("Opcion 0: Cerrar el programa.")


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

casos = open("Casos-nuevos-totales-por-region.txt" , "r")

leido = casos.readlines()   
personascovid = casosN(leido)


casos.close()  
    
def examenesP(lineaS):
        
    region = []
    fechasE = lineaS[0].split(',')
    
    i = 1
    while(i < len(lineaS)):
        lineaSnueva = lineaS[1].split(',')
        j = 3 
        examenesScovid = {}
        while(j<len(lineaSnueva)):
            examenesScovid[fechasE[j]] = lineaSnueva[j]
            j = j + 1
        region.append(examenesScovid)
        i = i + 1
    return region

examenes = open("Examenes-PCR-region.txt", "r")

leidoS = examenes.readlines()
examenesScovid = examenesP(leidoS)
     
    

examenes.close()

def pacientesU(lineasU):
    
    region = []
    fechasU = lineasU[0].split(',')
    
    i = 1
    while(i < len(lineasU)):
        lineaUnueva = lineasU[1].split(',')
        j = 3
        pacienteUcovid = {}
        while(j < len(lineaUnueva)):
            pacienteUcovid[fechasU[j]] = lineaUnueva[j]
            j = j + 1
        region.append(pacienteUcovid)
        i = i + 1
    return region

pacientesUCI = open("Pacientes-UCI-region.txt" , "r")

leidoU = pacientesUCI.readlines()
pacienteUcovid = pacientesU(leidoU)

                

pacientesUCI.close()



def Añoanterior(covid,UCI,PCR):
    actual = (input("ingrese fecha como yyyy-mm-dd: "))
    anterior= (input("Ingrese la fecha del año pasado que quiera comparar: "))
    
    region= int(input("ingrese la region: "))
    
    print("\n\n\t Resultados de el año actual \n")
    
    print("El numero de personas con covid positivo es: ",  covid[region][actual])
    
    print("El número de personas internadas en la UCI es: ", UCI[region][actual])
    
    print("La cantidad de examenes realizados fueron: ", PCR[region][actual])
    
    print("\n\n\t ----Totaldad del país---- \n")
  
    print("El número de personas con covid positivo a nivel país fue: ", covid[16][actual])

    PacientesUCI= 0
    ExamenesPCR= 0
    for i in range(1,16):
     PacientesUCI= PacientesUCI + int(UCI[i][actual])
    print("el numero de Pacientes UCI de ese dia nivel pais es", PacientesUCI)
    for i in range(1,16):
        ExamenesPCR= ExamenesPCR + int(PCR[i][actual])
    print("la cantidad de examenenes PCR de este dia a nivel pais es", ExamenesPCR)
    
    print("\n\n\t ---Resultados año anterior--- \n")
    print("El número de pacientes positivos en el año pasado fue de: ",  covid[region][anterior])
    print("El número de personas internados en la UCI el año pasado fue de: ",  UCI[region][anterior])
    print("La cantidad de examenes PCR realizados el año pasado fueron de: ",  PCR[region][anterior])
    print("\n\n\t ---Resultados nacionales año anteriror--- \n")
    print("el numero de personas positivos en covid del año pasado a nivel pais fue de: ",  covid[16][anterior])
    PacientesUCI= 0
    PacientesPCR= 0
    for i in range(1,16):
     PacientesUCI= PacientesUCI + int(UCI[i][anterior])
    print("el numero Pacientes UCI del dia del año pasado a nivel pais es", PacientesUCI)
    for i in range(1,16):
        PacientesPCR= PacientesPCR + int(PCR[i][anterior])
    print("la cantidad de examenes PCR del dia del año pasado  a nivel pais es", PacientesPCR)
    
def positividad(covid,PCR):#Requerimiento 3
    fecha= (input("ingrese fecha yyyy-mm-dd:"))
    Pcovid = 0
    examenPCR = 0
    for i in range(1,16):
     Pcovid= Pcovid + int(covid[i][fecha])
    print("Los pacientes positivos son:", Pcovid)
    for i in range(1,16):
     examenPCR = examenPCR + int(PCR[i][fecha])
    print("Los examenes PCR son:", examenPCR)
    Porcentaje = (Pcovid/examenPCR)*100
    print("el porcentaje de positividad es de un:",round(Porcentaje),"%")

regiones()
menu()
respuesta = int(input("Ingrese la opcion que desea: "))


while(respuesta != 0):
    if respuesta == 1:
        x = int(input("Ingrese la region: "))
        y = input("Ingrese la fecha yyyy-mm-dd:")
        positivo = personascovid[x][y]
        print("Las personas con covid positivo son: ", positivo)
    elif respuesta == 2:
        x = int(input("Ingrese la region: "))
        y = input("Ingrese la fecha yyyy-mm-dd:")
        UCI = pacienteUcovid[x][y]
        print("Las personas ingreasada en UCI son: ", UCI)
    elif respuesta == 3:
        print("[3] Tasa de positividad promedio por día determinado", positividad(personascovid,examenesScovid))
    elif respuesta == 4:
        print("[2]Comparacion de Covid positivos, paciente UCI y exámenes PCR", Añoanterior(personascovid,pacienteUcovid,examenesScovid))        
    menu()
    respuesta = int(input("Ingrese la opcion que desea: "))
    
print("Se cerro el programa: ")



