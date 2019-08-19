import os
from ser import rename

pokes = './pokes'
lista = []

#os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
#	print (f'{item}.png')

for file in os.listdir(pokes):
	item = rename(file)
	print(f"tranferindo {file} para {item}.jpg")
	os.rename(f"{pokes}/{file}", f"./pokemons/{item}.jpg")

#for item in lista:
#	print item

