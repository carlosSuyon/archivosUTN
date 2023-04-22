esPrimo::Integer ->Bool 

esPrimo x 
	| aux_primo (x list) == [True] =True
	| otherwise = False 
      where list  =[ y |y  <-[1..sqrt(x)]]


aux_primo:: [Float]->Integer->[Bool]

aux_primo [] x = []
aux_primo (y:ys) x
	 | (mod y x ) > 0 = [] ++aux_primo (ys x) 
	 | (mod  y x )== 0 =[True] 
	 | otherwise = aux_primo (ys x ) 