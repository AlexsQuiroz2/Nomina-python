import re
print('Buen día usuario por favor registre la siguiente información')
smlv = 1000000
sub = 117100
descuento_s = 4
descuento_p = 4



documento = str (input ("Numero de Documento: " ))
nombre = re.findall("[a-zA-Z]", input ("Nombres: " ))  
apellidos = re.findall("[a-zA-Z]", input ("Apellidos: " )) 
salario = int (input("Digite su salario minimo: " ))
dias = int (input('¿Cuantos dias trabajo?:'))



valor_dia = salario/30
valor_total_dia = int (valor_dia * dias)
valor_total_sub = sub * dias / 30
valor_descuento_s = salario * 0.04
valor_descuento_p = salario * 0.04
valor_total = valor_total_dia + valor_total_sub - valor_descuento_s - valor_descuento_p

print ("el señor/a", nombre, apellidos, "Con el numero de documento", documento, "cuenta con los siguentes valores respectivos a su pago de nomina segun los dias trabajados")
print ("Su salario es de: ", salario)
print ("El valor del subsidio de transporte es de: ", sub)
print ("la cantidad de dias que trabajo es de: ",dias )
print ("El valor que va a recibir por lo dias trabajados: ", valor_total_dia)
print ("El valor actual del subsidio es de: ", sub)
print ("Su valor del subsidio de transporte es de: ", valor_total_sub)
print ("El valor a descontar de salud es de: ", valor_descuento_s)
print ("El valor a descontar de pensión es de: ", valor_descuento_p)
print ("Tu total a recibir es: ", valor_total)
