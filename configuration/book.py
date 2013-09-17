from collections import OrderedDict
import codecs

class SingleFileSection(object):
  
  def __init__(self, title, file_name):
    self.__title__ = title
    self.__file_name__ = file_name
    
  def getTitle(self):
    return self.__title__
    
  def getText(self):
    return codecs.open(self.__file_name__, encoding='utf-8').read()
    
class CareerSection(object):
  
  def __init__(self, title, file_names):
    self.__title__ = title
    self.__file_names__ = file_names
    
  def getTitle(self):
    return self.__title__
    
  def getText(self):
    careers = []
    for file_name in self.__file_names__:
      careers.append(codecs.open(file_name, encoding='utf-8').read())
    return '/n'.join(careers)
    
class Book(object):
  
  def __init__(self, sections):
    self.__sections__ = OrderedDict()
    for section in sections:
      self.__sections__[section.getTitle()] = section
      
  def getSectionByTitle(self, title):
    return self.__sections__[title].getText()
    
  def getSectionTitles(self):
    return self.__sections__.keys()