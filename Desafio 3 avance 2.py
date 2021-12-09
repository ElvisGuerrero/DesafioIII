#Las proximas 4 funciones que se definen son donde se buscan datos dentro de los 3 archivos entregados del desafio.

def casosN(lineas):#[[Region, fecha1, fech2],[nombreregion,fecha1, fecg2linea2],linea3,etc]
	
	region = []
	fechas = lineas[0].split(',') # primera linea que tiene las fechas
	
	
	i = 1
	while (i < len(lineas)):
		lineanueva = lineas[i].split(',') # cuando i = 1, estamos hablando de la segunda linea del archivo
		j = 1 # partimos del segundo campo que es donde inician las fechas en este archivo
		personasCovid = {}
		while(j < len(lineanueva)):
			if lineanueva[j] != "":
				personasCovid[fechas[j]]=lineanueva[j]
			else:
				personasCovid[fechas[j]] = "0"
			j = j + 1
		region.append(personasCovid)
		i = i + 1
	
	return region

def casosUCI(lineas):#[linea1,linea2,linea3,etc]
	
	region = []
	fechas = lineas[0].split(',') # primera linea que tiene las fechas
	
	
	i = 1
	while (i < len(lineas)):
		lineanueva = lineas[i].split(',') # cuando i = 1, estamos hablando de la segunda linea del archivo
		j = 3 # partimos del cuarto campo que es donde inician las fechas en este archivo
		personasCovid = {}
		while(j < len(lineanueva)):
			if lineanueva[j] != "":
				personasCovid[fechas[j]]=lineanueva[j]
			else:
				personasCovid[fechas[j]] = "0"
			j = j + 1
		region.append(personasCovid)
		i = i + 1
	
	return region
	
def examenesPCR(lineas):#[linea1,linea2,linea3,etc]
	
	region = []
	fechas = lineas[0].split(',') # primera linea que tiene las fechas
	
	
	i = 1
	while (i < len(lineas)):
		lineanueva = lineas[i].split(',') # cuando i = 1, estamos hablando de la segunda linea del archivo
		j = 3 # partimos del cuarto campo que es donde inician las fechas en este archivo
		personasCovid = {}
		while(j < len(lineanueva)):
			if lineanueva[j] != "":
				personasCovid[fechas[j]]=lineanueva[j]
			else:
				personasCovid[fechas[j]] = "0"
			j = j + 1
		region.append(personasCovid)
		i = i + 1
	
	return region

def Poblacion(lineas):#[linea1,linea2,linea3,etc]
	
	region = []
	
	i = 1
	totalpais = 0
	while (i < len(lineas)):
		lineanueva = lineas[i].split(',')# cuando i = 1, estamos hablando de la segunda linea del archivo
		region.append(int(lineanueva[2]))
		totalpais = totalpais + int(lineanueva[2])
		i = i + 1
	
	region.append(totalpais)
	
	return region

#Aqui se define el procesamiento de los archivos entregados, donde se abren los archivos, como cerrarlos para que no existan problemas.
	
def ProcesoDeDatos():

	leercovid = open("Casos-nuevos-totales-por-region.txt", "r")
	leidoCovid = leercovid.readlines() 
	leercovid.close()
	leerPCR = open("Examenes-PCR-region.txt", "r")
	leidoPCR = leerPCR.readlines() 
	leerPCR.close()
	leerUCI = open("Pacientes-UCI-region.txt", "r")
	leidoUCI = leerUCI.readlines() 
	leerUCI.close()
	
	
	personasCovid = casosN(leidoCovid) 
	personasPCR = examenesPCR(leidoPCR)
	personasUCI = casosUCI(leidoUCI)
	PersonasRegion = Poblacion(leidoPCR)

	return personasCovid,personasPCR, personasUCI, PersonasRegion

#Aqui se definen menus, como el listado de las regiones como sus respectivos codigos de uso. 
	
def Regiones():
	print ("Arica y Parinacota --> 0")
	print ("Tarapacá --> 1")
	print ("Antofagasta --> 2")
	print ("Coquimbo --> 3")
	print ("Valparaíso --> 4")
	print ("Metropolitána --> 5")
	print ("O’Higgins --> 6")
	print ("Maule --> 7")
	print ("Ñuble --> 8")
	print ("Biobío --> 9")
	print ("Araucanía --> 10")
	print ("Los Ríos --> 11")
	print ("Los Lagos --> 12")
	print ("Aysén --> 13")
	print ("Magallanes --> 14\n\n\n")

def menu():
	print("Bienvenido usuario, en el menu se muestran las opciónes disponibles para su uso. ")
	print("Opción 1: Mostrar casos Covid+, casos UCI y los examenes PCR de un día determinado. ")
	print("Opción 2: Comparacion de casos Covid+, casos UCI y examenes PCR con una fecha anterior. ")
	print("Opción 3: Mostrar una tasa de positividad en un día determinado. ")
	print("Opción 4: Mostrar la tasa de positividad de un Mes determinado")
	print("Opción 5: Mostrar la relacion de la poblacion de una región con la cantidad de Covid+. ")
	print("Opción 6: Mostrar el TOP de los 10 dias con mas casos Covid+ de una región determinada. ")
	print("Opción 9: Cerrar el programa. ")
    
    
	respuesta = int(input("Ingrese la opción que desea escoger: "))
	
	return respuesta

def NR(cod):
	dicCodReg = {
		0: "Arica y Parinacota",
		1: "Tarapacá",
		2: "Antofagasta",
		3: "Coquimbo",
		4: "Valparaíso",
		5: "Metropolitána",
		6: "O’Higgins",
		7: "Maule",
		8: "Ñuble",
		9: "Biobío",
		10: "Araucanía",
		11:"Los Ríos",
		12: "Los Lagos",
		13: "Aysén",
		14: "Magallanes",
		15: "Chile"
		}
	return dicCodReg[cod]

#Aqui esta definida el primer requerimiento en donde mustra casos covid+, ingresados UCI, como examenes PCR.
	
def PlanosC(personasCovid,personasPCR, personasUCI,regionsolicitada,fechasolicitada):
	
	# CovidPositivo
	if fechasolicitada in personasCovid[regionsolicitada].keys(): 
		print("El día ",fechasolicitada," se registraron ",personasCovid[regionsolicitada][fechasolicitada], " personas Covid Positivo en la Región de ",NR(regionsolicitada))
		covidPais = 0
		for i in range(0,15):
			covidPais = covidPais + int(personasCovid[i][fechasolicitada])
		print("Además, a nivel país, el día ",fechasolicitada," se registraron ",covidPais, " personas Covid Positivo")
	else:
		print("No registramos datos personas Covid positivo para la fecha ", fechasolicitada) 
	# PCR
	if fechasolicitada in personasPCR[regionsolicitada].keys(): 
		print("El día ",fechasolicitada," se registraron ",personasPCR[regionsolicitada][fechasolicitada], " exámenes PCR en la Región de ",NR(regionsolicitada))
		pcrPais = 0
		for i in range(0,15):
			pcrPais = pcrPais + int(personasPCR[i][fechasolicitada])
		print("Además, a nivel país, el día ",fechasolicitada," se registraron ",pcrPais, " exámenes PCR")
	else:
		print("No registramos datos de exámenes PCR para la fecha ", fechasolicitada)
	# UCI
	if fechasolicitada in personasUCI[regionsolicitada].keys(): 
		print("El día ",fechasolicitada," se registraron ",personasUCI[regionsolicitada][fechasolicitada], " personas en UCI en la Región de ",NR(regionsolicitada))
		uciPais = 0
		for i in range(0,15):
			uciPais = uciPais + int(personasUCI[i][fechasolicitada])
		print("Además, a nivel país, el día ",fechasolicitada," se registraron ",uciPais, " personas en UCI")
	else:
		print("No registramos datos de personas en UCI para la fecha ", fechasolicitada)

#Aqui se compara los casos Covid+, como los ingresados UCI y los examenes PCR con una fecha del año anterior si se tiene los registros.
	
def Añoanterior(personasCovid,personasPCR, personasUCI,regionsolicitada,fechasolicitada):
	
	fechaTemp = fechasolicitada.split("-")
	fechapasada = str(int(fechaTemp[0]) - 1) + "-" + fechaTemp[1] + "-" + fechaTemp[2]
	
	PlanosC(personasCovid,personasPCR, personasUCI,regionsolicitada,fechasolicitada)
	PlanosC(personasCovid,personasPCR, personasUCI,regionsolicitada,fechapasada)
	
#Esta definida en esta funcion la positividad de un dia determinado de un año y mes determinado.

def positividad1(personasCovid,personasPCR, personasUCI,regionsolicitada,fechasolicitada):
	
	
	if fechasolicitada in personasCovid[regionsolicitada].keys() and fechasolicitada in personasPCR[regionsolicitada].keys(): 
		num = int(personasCovid[regionsolicitada][fechasolicitada])
		den = int(personasUCI[regionsolicitada][fechasolicitada])
		if den == 0:
			res = 0
		else:
			res = round((num/den),2)
		
		print("El día ",fechasolicitada," la tasa de positividad fué ",res, "% en la Región de ",NR(regionsolicitada))
		covidPais = 0
		pcrPais = 0
		for i in range(0,15):
			covidPais = covidPais + int(personasCovid[i][fechasolicitada])
			pcrPais = pcrPais + int(personasPCR[i][fechasolicitada])
		if pcrPais ==0:
			resP = 0
		else:
			resP = round((covidPais/pcrPais),2)
			
		print("Además, a nivel país, el día ",fechasolicitada," la tasa de positividad fué de ",resP, " %")
	else:
		print("No podemos calcular la tasa de positividad porque faltán datos para la fecha ", fechasolicitada)
		
	return res,resP

#Aqui al contrario de la funcion anterior, se define la positividad de un més completo.

def positividad2(personasCovid,personasPCR, personasUCI,regionsolicitada,fechasolicitada):
	

	
	positividadR = 0
	positividadP = 0
	dias = 0
	
	
	for key in personasCovid[regionsolicitada].keys():
		
		if fechasolicitada == key[0:7]: 
			posR, posP = positividad1(personasCovid,personasPCR, personasUCI,regionsolicitada,key)
			positividadR = positividadR + posR
			positividadP = positividadP + posP
			dias = dias + 1
		
	print(" La positividad promedio del mes ", fechasolicitada,", es ", positividadR/dias, " en la región de ", NR(regionsolicitada))
	print(" Además, a nivel país, el promedio de positividad en el mes ",fechasolicitada," ad fué de ",positividadP/dias, " %")

#Aqui se define la relacion de poblacion que un dato que se encuentra en los archivos entregados con la cantidad de casos Covid+.
	
def Rcovid(personasCovid,personasPCR, personasUCI,fechasolicitada, PersonasRegion):
		
	relacion = {}
	relacioninvertida = {}
	valores = []
	i = 0
	while(i < len(PersonasRegion)-1):
		relacion[NR(i)] = int(personasCovid[i][fechasolicitada])/PersonasRegion[i] 
		relacioninvertida [int(personasCovid[i][fechasolicitada])/PersonasRegion[i]] = NR(i)
		valores.append(int(personasCovid[i][fechasolicitada])/PersonasRegion[i])
		i = i + 1
	

	ordenado = sorted(valores)
	
	for valor in ordenado:
		#if valor es menor al valor nacional:
		print("La relación COVID / Población en la región ", relacioninvertida[valor], " para el día ", fechasolicitada, " es ", valor)
		

#Aqui se muestra la mayor positividad de un año en especifico de una region en especifico.

def Mpositividad(personasCovid,personasPCR, personasUCI,regionsolicitada,fechasolicitada):
	
	
	
	covidyeardato = []
	covidyeardia = []
	
	
	for key in personasCovid[regionsolicitada].keys():
		
		if fechasolicitada == key[0:4]:
			covidyeardato.append(int(personasCovid[regionsolicitada][key]))
			covidyeardia.append(key)
			
		
	i = 0
	
	while(i < len(covidyeardato)):
		j = i
		while(j < len(covidyeardato)):
			
			if covidyeardato[i] <  covidyeardato[j]:
				
				temp= covidyeardato[i]
				covidyeardato[i] = covidyeardato[j]
				covidyeardato[j] = temp
				
				temp2= covidyeardia[i]
				covidyeardia[i] = covidyeardia[j]
				covidyeardia[j] = temp2
			j = j + 1
    
		i = i + 1
	
	dias = 0
	
	while(dias < 10):
		print(covidyeardia[dias], covidyeardato[dias])
		dias = dias + 1
		
#Aqui se definen almacenes de datos que se usan luego para llamarlos dentro de la ejecucion de programa.
#Almacen de Datos del programa-------------------------------------------------	
   
def datos():
	print("Ingrese Región: ")
	Regiones()
	regionsolicitada = int(input("Ingrese la region que desea ver: "))
	print("Ingrese la fecha a evaluar. Use el siguiente formato: yyyy-mm-dd\n\n")
	fechasolicitada = input()
	
	return regionsolicitada,fechasolicitada
	
def datosmes():
	print("Ingrese Región: ")
	Regiones()
	regionsolicitada = int(input("Ingrese la region que desea ver: "))
	print("Ingrese la fecha a evaluar. Use el siguiente formato: yyyy-mm \n\n")
	fechasolicitada = input()
	
	return regionsolicitada,fechasolicitada

def datosregion():
	print("Ingrese la fecha a evaluar. Use el siguiente formato: yyyy-mm \n\n")
	fechasolicitada = input()
	
	return fechasolicitada

def datosyear():
	print("Ingrese Región: ")
	Regiones()
	regionsolicitada = int(input("Ingrese la region que desea ver: "))
	print("Ingrese la fecha a evaluar. Use el siguiente formato: yyyy \n\n")
	fechasolicitada = input()
	
	return regionsolicitada,fechasolicitada

#Aqui es donde se ejecuta el programa y donde el usuario ingresa los datos de entrada para luego ejecutar las funciones que el desee.
#Ejecucion---------------------------------------------------------------------

personasCovid,personasPCR, personasUCI, PersonasRegion = ProcesoDeDatos()

respuesta = menu()
while(respuesta != 9):
	
	if respuesta == 1:
		regionsolicitada, fechasolicitada = datos()
		PlanosC(personasCovid,personasPCR, personasUCI,regionsolicitada,fechasolicitada)
	elif respuesta == 2:
		regionsolicitada, fechasolicitada = datos()
		Añoanterior(personasCovid,personasPCR, personasUCI,regionsolicitada,fechasolicitada)
	elif respuesta ==3:
		regionsolicitada, fechasolicitada = datos()
		res, resP = positividad1(personasCovid,personasPCR, personasUCI,regionsolicitada,fechasolicitada)
	elif respuesta ==4:
		regionsolicitada, fechasolicitada = datosmes()
		positividad2(personasCovid,personasPCR, personasUCI,regionsolicitada,fechasolicitada)
	elif respuesta ==5:
		fechasolicitada = datosregion()
		Rcovid(personasCovid,personasPCR, personasUCI,fechasolicitada, PersonasRegion)
	elif respuesta ==6:
		regionsolicitada, fechasolicitada = datosyear()
		Mpositividad(personasCovid,personasPCR, personasUCI,regionsolicitada,fechasolicitada)
	
	respuesta = menu()

print("Se cerro el programa. Gracias por usar nuestro programa. ")





