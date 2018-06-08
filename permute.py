
def permute(lista, start, end):
	
	if start == end:
		
		print lista
	
	else:
		
		for i in range(start, end + 1):
			
			lista[i], lista[start] = lista[start], lista[i]
			permute(lista, start + 1, end)
			lista[i], lista[start] = lista[start], lista[i]


permute([1,2,3],0,2)
