# função que transforma o nome do arquivo no nome ordinal.
def rename(filename):
	numero = ""
	for caractere in filename:
		try:
			n = int(caractere)
			numero = numero + caractere
		except Exception as inst:
			break
	
	return numero