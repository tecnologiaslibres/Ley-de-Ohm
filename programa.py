#Ley de ohm (el programa aun esta en desarrollo)

print "Para calcular voltaje presione 1"
print "Para calcular amperaje presione 2"
print "Para calcular resistencia presione 3"
valor = int(input("Ingrese la opcion: "))
def comprobarDatos():
	if (valor>0) or (valor<=3):
		print ("Usted tecleo " + str(valor) + " Por favor, elija las opciones correctamente")
		return
comprobarDatos()
# Calcular voltaje
if valor == 1:
	amperaje = float(input("Ingrese amperes: "))
	resistencia = float(input("Ingrese resistencia: "))
#Formula
	voltaje = resistencia*amperaje
	print (str(voltaje)+" volts")

# Calcular amperaje

if valor == 2:
	voltaje = float(input("Ingrese voltaje: "))
	resistencia = float(input("Ingrese resistencia: "))
#Formula
	amperaje = voltaje / resistencia
	print (str(amperaje) + " ampers")

# Calcular resistencia

if valor == 3:
	voltaje = float(raw_input("Ingrese voltaje: "))
	amperaje = float(raw_input("Ingrese amperaje: "))
	resistencia = voltaje / amperaje
#Formula
	print (str(resistencia) + " omhs")
