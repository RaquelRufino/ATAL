

def isSolution(lista, k):
	
	return (k + 1) == len(lista)

def processSolution(lista,k):
	
	print "{",
	for i in range(len(k)):
		if lista[i]:
			print " " + i 
	
	print "}"


def constructCandidates(lista,k):
	
	c = []
	c.append(False)
	c.append(True)
	return c


