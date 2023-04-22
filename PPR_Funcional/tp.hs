triangular a b c 
		 | (a<(b+c) && b<(a+c) && c<(a+b))=True
		 |otherwise = False


areaTriangulo  a b c 
		| s >0 = sqrt (s(s - a)(s - b)(s - c)) 
		|otherwise = 0
	       where  s = ((a+b+c)/2)