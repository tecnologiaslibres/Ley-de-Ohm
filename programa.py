# Calculo de Ley de Ohm
def menu():
	try:
		print (" ")
		print ("==================================+")
		print (" ")
		print "Para calcular voltaje presione 1"
		print (" ")
		print "Para calcular amperaje presione 2"
		print (" ")
		print "Para calcular resistencia presione 3"
		print (" ")
		print "Para salir presione 4"
		print (" ")
		print ("==================================+")
		print (" ")
		return input ("Ingrese la opcion: ")
		print "hola"
	except NameError:
		print (" ")
		print ("===================================+")
		print "Tiene que ingresar un valor numerico"
		print ("===================================+")
		print (" ")
	except SyntaxError:
		print (" ")
		print ("===================================+")
		print "Por favor, ingrese un valor entre 1 y 3"
		print ("===================================+")
		print (" ")
loop = 1
valor = 0
while loop == 1:
	valor = menu()
#Calcular voltaje
	if valor == 1:
		print (" ")
		print ("========================+")
		print ("Ud. calculara el voltaje")
		print ("========================+")
		print (" ")

		while True:
			try:
				amperaje = float(raw_input("Ingrese el amperaje: "))
				break
			except ValueError:
				print (" ")
				print ("===================================+")
				print "Tiene que ingresar un valor numerico"
				print ("===================================+")
				print (" ")

		while True:
			try:
				resistencia = float(raw_input("Ingrese la resistencia: "))
				break
			except ValueError:
				print (" ")
				print ("===================================+")
				print "Tiene que ingresar un valor numerico"
				print ("===================================+")
				print (" ")
# Formula
		voltaje = resistencia * amperaje
		print (" ")
		print ("============+")
		print (str(voltaje)+" volts")
		print ("============+")
		print (" ")
		raw_input('Presion una tecla para continuar...')

# Calcular amperaje
	if valor == 2:
		print (" ")
		print ("========================+")
		print ("Ud calculara el amperaje")
		print ("========================+")
		print (" ")
		while True:
			try:
				voltaje = float(raw_input("Ingrese los volts: "))
				break
			except ValueError:
				print (" ")
				print ("===================================+")
				print "Tiene que ingresar un valor numerico"
				print ("===================================+")
				print (" ")
		while True:
			try:
				resistencia = float(raw_input("Ingrese la resistencia: "))
				break
			except ValueError:
				print (" ")
				print ("===================================+")
				print "Tiene que ingresar un valor numerico"
				print ("===================================+")
				print (" ")

# Formula
		def DeFamperaje():
			while True:
				try:
					amperaje = voltaje / resistencia
					print "valores"
					return amperaje
				except ZeroDivisionError:
					print (" ")
					print ("===========================================+")
					print "Tiene que ingresar un valor distinto de cero"
					print ("===========================================+")
					print (" ")

					break
		amperaje = DeFamperaje()
		print (" ")
		print ("============+")
		print (str(amperaje) + " ampers")
		print ("============+")
		print (" ")
		raw_input('Presion una tecla para continuar...')

# Calcular resistencia

	if valor == 3:
		print (" ")
		print ("============================+")
		print ("Ud. calculara la resistencia")
		print ("============================+")
		print (" ")

		while True:
			try:
				voltaje = float(raw_input("Ingrese voltaje: "))
				break
			except ValueError:
				print (" ")
				print ("===================================+")
				print "Tiene que ingresar un valor numerico"
				print ("===================================+")
				print (" ")
		while True:
			try:
				amperaje = float(raw_input("Ingrese amperaje: "))
				break
			except ValueError:
				print (" ")
				print ("===================================+")
				print "Tiene que ingresar un valor numerico"
				print ("===================================+")
				print (" ")
# Formula
		def DeFresistencia():
			while True:
				try:
					resistencia = voltaje / amperaje
					return resistencia
				except ZeroDivisionError:
					print (" ")
					print ("===========================================+")
					print "Tiene que ingresar un valor distinto de cero"
					print ("===========================================+")
					print (" ")

					break
		resistencia = DeFresistencia()
		print (" ")
		print ("============+")
		print (str(resistencia) + " omhs")
		print ("============+")
		print (" ")
		raw_input('Presion una tecla para continuar...')

	if valor == 4:
		break

#	else: 
#		print (" ")
#		print ("=============================+")
#		print "No ingreso una opcion correcta"
#		print ("=============================+")
#		print (" ")
loop = 0
print (" ")
print ("==============================+")
print "Fin de programa de demostracion"
print ("==============================+")
print (" ")
