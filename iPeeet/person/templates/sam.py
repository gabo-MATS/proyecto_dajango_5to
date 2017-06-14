notas=[]
ss=1
contador=[0,0,0,0,0,0,0,0,0,0]
moda=1

while ss<=6:
	print("1.-Ingrese un valor del 1 al 99")
	print("2.-Graficar el histograma")
	print("3.-Mostrar mayor y menor")
	print("4.-Mostrar el promedio")
	print("5.-Mostrar la moda")
	print("salir")
	ss=int(input("Ingrese una opcion: "))

	if ss==1:
		nota = int(input("ingrese numeros del 1 al 99"))
		nota.append(nota)
		if nota >=0 and <=10:
			contador[0] +=1
		if nota >=10 and <=20:
			contador[0] +=1



	if ss==2:
		for i in range(len(contador)):
			print (i*10, "-", (i*10+10), "*" (contador[ï])))