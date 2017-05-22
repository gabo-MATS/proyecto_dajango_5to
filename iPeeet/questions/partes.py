opcion=3

while opcion !=6:
	print("Menu:")
	print("1. Resta")
	print("2. Suma")
	print("3. Multiplicaion")
	print("4. Division")
	print("5. Salir")

	opcion=int(input("Ingrese una opcion: "))

	f=int(input("Ingrese f: "))
	e=int(input("Ingrese e: "))

	if opcion==1:
		print(f-e)
	elif opcion==2:
		print(f+e)
	elif opcion==3:
		print(f*e)
	elif opcion==4:
		print(f/e)

print("¡Gracias por colaborar!")

