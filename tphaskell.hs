--punto 1--
triangular a b c 
		 | (a<(b+c) && b<(a+c) && c<(a+b))=True
		 |otherwise = False

--punto 2 --
areaTriangulo  a b c 
	| triangular a b c ==True =sqrt (s*(s - a)*(s - b)*(s - c) )
	|otherwise = 0
	 
   where s = (a+b+c)/2
--punto 3 --
finalizaPrimerDigito::Integer ->Bool
finalizaPrimerDigito x = aux_finalizaPrimerDig (show (x)) 



aux_finalizaPrimerDig::[Char]->Bool

aux_finalizaPrimerDig(x:xs)
				| x == last xs  =True
				|otherwise = False

--punto 4 -- 
{-
nuevalista x =[y| y <-[2.. (raiz x)]]

raiz x = round (x ** 0.5)


aux_primo x [] = [True]
aux_primo x (y:ys)
	| (mod x y == 0 )==True =[False]
	| otherwise = []++ aux_primo x ys

primo x 
	| (z ==[True]) =True
	|otherwise = False
   where  z = aux_primo x (nuevalista (x))


primosEnIntervalo::Int->Int->[Int]
primosEnIntervalo x y = [z| z<- [x..y], primo x , primo y]-}



--punto 5 --

siguiente x 
	| even x ==True =  (x `div` 2)
	| otherwise = (1+ 3* x) 


collatz   1   list = list
collatz x list
	  | z:[] ++ z  list 
          where z = siguiente x 