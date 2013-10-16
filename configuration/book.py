from collections import OrderedDict
import codecs
import configuration.site
import xml.etree.ElementTree as ET
import jinja2

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
    
  def getCareers(self):
    if not hasattr(self, '__careers__'):
      self.__careers__ = []
      for file_name in self.__file_names__:
        for career in Career.fromFile(file_name):
          self.__careers__.append(career)
          
    return self.__careers__
    
  def getCareerNames(self):
    return [career.getName() for career in self.getCareers()]
    
class Book(object):
  
  def __init__(self, sections):
    self.__sections__ = OrderedDict()
    for section in sections:
      self.__sections__[section.getTitle()] = section
      
  def getSectionByTitle(self, title):
    return self.__sections__[title]
    
  def getSectionTitles(self):
    return self.__sections__.keys()

class Move(object):
  
  def __init__(self, name, body):
    self.__name__ = name
    self.__body__ = body
    
  def getName(self):
    return self.__name__
    
  def getBody(self):
    return self.__body__
    
class Career(object):
  
  @staticmethod
  def fromFile(file_name):
    tree = ET.parse(file_name)
    for career_node in tree.getroot().findall('career'):
      yield Career(name=career_node.find('name').text,
                   stats=career_node.find('stats').text,
                   description=career_node.find('description').text,
                   recovery=career_node.find('recovery').find('movebody').text,
                   move_instructions=career_node.find('moveinstructions').text,
                   moves=[Move(move.find('movename').text, move.find('movebody').text) for move in career_node.find('moves').findall('move')],
                   history=[event.text for event in career_node.find('history').findall('event')]
                  )
                  
  def __init__(self, name, stats, description, recovery, move_instructions, moves, history):
    self.__name__ = name
    self.__stats__ = stats
    self.__description__ = description
    self.__recovery__ = recovery
    self.__move_instructions__ = move_instructions
    self.__moves__ = moves
    self.__history__ = history
    
  def getName(self):
    return self.__name__
  
  def getStats(self):
    return self.__stats__
    
  def getDescription(self):
    return self.__description__
    
  def getRecovery(self):
    return self.__recovery__
  
  def getMoveInstructions(self):
    return self.__move_instructions__
    
  def getMoves(self):
    return self.__moves__
    
  def getHistory(self):
    return self.__history__
