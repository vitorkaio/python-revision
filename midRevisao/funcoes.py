#coding: utf-8

# verifica se um valor existe na lista, caso sim retorna True, caso contrário retorna False
def isExistsInList(lista, valor):
  try:
    verify = lista.index(valor)
    return True
  except ValueError as err:
    return False

def removeItemForList(lista, valor):
  try:
    lista.remove(valor)
    return True
  except ValueError as err:
    return False

def imprimeLista(lista):
  print(str(lista))