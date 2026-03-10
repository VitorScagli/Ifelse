# Multiplicaçao e Divisao com IF
# 10/03/2026

op = input("Digite 1- SOMA 2- SUBTRAÇAO 3- MUTIPLICAÇAO 4- DIVISAO 5- POTENCIAÇAO 6- RADICIAÇAO")
op = int(op)

a = input("Entre com o 1º numero")
a = int(a)

b = input ("Entre com o 2º numero")
b = int(b)

if (op == 1):
	print(a + b)
elif (op == 2):
	print (a - b)
elif (op == 3):
	print (a * b)
elif (op == 4):
	print (a / b)
elif (op == 5):
	print ( a ** b)
elif (op == 6 ):
	print (a ** (1/b))
else:
	print("Digite uma opçao valida")
input()