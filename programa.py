#Ley de ohm
from __builtin__ import int
global valor
global voltaje
global amperaje
global resistencia

print "Para calcular voltaje presione 1"
print "Para calcular amperaje presione 2"
print "Para calcular resistencia presione 3"
valor = int(input("Ingrese la opcion: "))
#Calcular voltaje
if valor == 1:
    print ("Ud. calculara el voltaje")
    print ("========================")
    amperaje = float(input("Ingrese amperes: "))
    resistencia = float(input("Ingrese resistencia: "))
#Formula
    voltaje = resistencia * amperaje
    print (str(voltaje)+" volts")
# Calcular amperaje
if valor == 2:
    print ("Ud calculara el amperaje")
    print ("========================")
    resistencia = float(input("Ingrese resistencia: "))
#formula
    amperaje = voltaje / resistencia
    print (str(amperaje) + " ampers")
# Calcular resistencia

if valor == 3:
    print ("Ud. calculara la resistencia")
    print ("============================")
    voltaje = float(raw_input("Ingrese voltaje: "))     
    amperaje = float(raw_input("Ingrese amperaje: "))
#formula
    resistencia = voltaje / amperaje
    print (str(resistencia) + " omhs")
else:
    print ("Ud ingreso " + str(valor) + " Por favor ingrese la opcion correcta")
