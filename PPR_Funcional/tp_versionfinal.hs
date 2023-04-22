triangular a b c 
		 | (a<(b+c) && b<(a+c) && c<(a+b))=True
		 |otherwise = False


areaTriangulo  a b c 
	| triangular a b c ==True =sqrt (s*(s - a)*(s - b)*(s - c) )
	|otherwise = 0
	 
   where s = (a+b+c)/2


deDig_a_String::Integer ->String
deDig_a_String x = show x 

aux_deDig_a_String::[Char]->Bool

aux_deDig_a_String(x:xs)
		| x == last xs  =True
		|otherwise = False

--numero primo --

list x = [y |y<-[2..x]]

esPrimo x 
	|funcion x list  (x** 0.5) ==[True] = True
	| funcion x list  (x** 0.5) ==[] = False
funcion x [] =[]
funcion x (y:ys)
	| ((mod x y) == 0)  == True =[True]
	| otherwise =[]++funcion x ys

--punto numero 2 , se trabaja solo con valores int--
semiperimentro ::Int -> Int->Int -> Int
semiperimentro:: a , b , c 
	| (a >0 )&& (b>0) && (c>0)==True = (a+b+c)/2
	|otherwise  = 0


area a b c 
	| (semiperimetro  a b c >0 ) && (z>0) = sqrt (z)
	|otherwise  = 0



	where z = (semiperimetro*(semiperimetro-a)*		  (semiperimetro-b)*(semiperimetro-c)

--punto 3 --
nuevalista x =[y| y <-[2.. x]]

raiz x = round (x ** 0.5)


aux_primo x [] = []
aux_primo x (y:ys)
	| (mod x y == 0 )==True =[True]
	| otherwise = []++ aux_primo x ys

primo x 
	| aux_primo x  nuevalista (raiz x) ==[True]  =True
	| aux_primo x  nuevalista (raiz x) ==[] = False 

--punto 5 --

siguiente x 
	| even x ==True =  (x `div` 2)
	| otherwise = (1+ 3* x) 

