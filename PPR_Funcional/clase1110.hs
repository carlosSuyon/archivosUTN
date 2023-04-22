--dada una lista de enteros devolver el penultimo elemento--



penultimo::[Int]->Int

penultimo (x:xs)
	|length (x:xs) ==2 =x
	|otherwise = penultimo (xs)


--dada una lista  y un valor de referencia genere otra lista solo con los cuadrados de los elementos que superan el valor recibido--
lista::[Int]->Int->[Int]
lista [] y = []
lista (x:xs) y
	| x > y =[z]++lista xs y 
	|otherwise = lista xs y 
       where z = x*x


--RESOLVER el mismo ejercicio de otra froma--
listaxcompresion::[Int]->Int->[Int]
listaxcompresion xs y = [x*x| x<- xs , x>= y]


-- genere una fucion dada una lista de ent genere otra list con los valores 'par' / 'impar'--

listaparidad::[Integer]->[String]

listaparidad xs =[validar x | x<-xs]

validar:: Integer ->String
validar x = if even x then "Par" else "Impar"
	 
--con funciones de orden superior--
lsita_parOS::[Integer] ->[String]
lsita_parOS xs = map validar xs

-- dadas dos listas genere una tercera con los elementos de la primera que se encuentren presente en la segunda --
existe::[Integer]->Integer->Bool
existe [] x = False
existe (x:xs) y 
	| x == y =True
	| otherwise= existe ys x

presentes::[Integer]-> [Integer]-> [Integer]
presentes xs ys = [x| x<- xs ,existe ys x ]
--dado un nro si es capicua o no --

capicua (x:xs)
	

	si la cant de digt es par 
		conver nro -> string
		