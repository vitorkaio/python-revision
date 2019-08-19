#coding: utf-8

import funcoes
from produto import Produto

def listAndDicts():
  lista = [1, 2, 3, 'kira', '99', 5]
  valor = 'kira'

  verify = funcoes.isExistsInList(lista, valor)

  if verify == True:
    remove = funcoes.removeItemForList(lista, valor)
    if remove == True:
      funcoes.imprimeLista(lista)
    else:
      print('Item not deleted')
  else:
    print('Item not found')

  print('\n Dicts \n')

  person = {'userName': 'kira', 'age': 20, 'online': True}
  # print(person['userName'])

  # interate in keys off dicts
  for chave in person.keys():
    print(person[chave])

  lis = ['name', 'cont', 'isHere']
  test = {lis[0]: 'Vih', lis[1]: 159, lis[2]: False}

  print(test)

if __name__ == "__main__":
  produto = Produto('Celular', 'The most powerful phone in the market', 350.65)
  print(produto.getName())
  print(produto.toDict())