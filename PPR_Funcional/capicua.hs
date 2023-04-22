numero_cadena::Integer ->String

numero_cadena x = show x 


aux_capicua ::[Char] ->Bool

aux_capicua (x:xs)
	| x == ultimo xs = True && aux_capicua (quitar_ultimo xs)
	|otherwise      =False

ultimo::[Char] -> Char
 
ultimo [x]= x
ultimo(_:xs) = ultimo xs 

capicua::Integer-> Bool

capicua x = aux_capicua(numero_cadena x)


quitar_ultimo::[char]->[char]
quitar_ultimo xs = take ((length xs)-1)xs
