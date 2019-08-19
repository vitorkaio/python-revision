#coding: utf-8

class Produto:
  def __init__(self, name, des, value):
    self.__name = name
    self.__des = des
    self.__value = value

  def setName(self, name):
    self.__name = name
  
  def getName(self):
    return self.__name

  def setDes(self, des):
    self.__des = des
  
  def getDes(self):
    return self.__des

  def setValue(self, value):
    self.__value = value
  
  def getValue(self):
    return self.__value

  def toDict(self):
    return {'name': self.__name, 'des': self.__des, 'value': self.__value}