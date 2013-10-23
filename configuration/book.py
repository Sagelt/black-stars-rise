from collections import OrderedDict
import codecs
import xml.etree.ElementTree as ET

def content(tag):
  if tag.text:
    return tag.text + ''.join(ET.tostring(e) for e in tag)
  else:
    return ''.join(ET.tostring(e) for e in tag)

class Chapter(object):
  
  def __init__(self, key, title, file_name):
    self.__key__ = key
    self.__title__ = title
    self.__file_name__ = file_name
    
  def getTitle(self):
    return self.__title__
    
  def getKey(self):
    return self.__key__
    
  def getHeaders(self):
    return [section.getTitle() for section in self.getSections()]
    
  def getSections(self):
    if not hasattr(self, '__sections__'):
      self.__sections__ = []
      for section in Section.fromFile(self.__file_name__):
        self.__sections__.append(section)
    return self.__sections__
    
class Section(object):
  
  @staticmethod
  def fromFile(file_name):
    tree = ET.parse(file_name)
    for section_node in list(tree.getroot()):
      yield Section(title=section_node.find('h1').text,
                    text=content(section_node))
                    
  def __init__(self, title, text):
    self.__title__ = title
    self.__text__ = text
    
  def getTitle(self):
    return self.__title__
    
  def getText(self):
    return self.__text__
    
class Setting(object):
  
  def __init__(self, key, title, file_names):
    self.__key__ = key
    self.__title__ = title
    self.__file_names__ = file_names
    
  def getTitle(self):
    return self.__title__
    
  def getKey(self):
    return self.__key__
    
  def getCareers(self):
    if not hasattr(self, '__careers__'):
      self.__careers__ = []
      for file_name in self.__file_names__:
        for career in Career.fromFile(file_name):
          self.__careers__.append(career)
          
    return self.__careers__
    
  def getCareerNames(self):
    return [career.getName() for career in self.getCareers()]
    
  def getSetups(self):
    if not hasattr(self, '__setups__'):
      self.__setups__ = []
      for file_name in self.__file_names__:
        for setup in Setup.fromFile(file_name):
          self.__setups__.append(setup)
    
    return self.__setups__
  
  def getSetupTitles(self):
    return [setup.getTitle() for setup in self.getSetups()]


class Book(object):
  
  def __init__(self, parts):
    self.__parts__ = OrderedDict()
    for part in parts:
      self.__parts__[part.getKey()] = part
      
  def getPartByKey(self, key):
    return self.__parts__[key]
    
  def getPartKeys(self):
    return self.__parts__.keys()
    
  def getParts(self):
    return self.__parts__.values()
    
  def getDefaultPartKey(self):
    return self.__parts__.keys()[0]


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
    for career_node in tree.getroot().iter('career'):
      yield Career(name=career_node.find('name').text,
                   stats=career_node.find('stats').text,
                   description=career_node.find('description').text,
                   recovery=career_node.find('recovery').find('movebody').text,
                   move_instructions=career_node.find('moveinstructions').text,
                   moves=[Move(move.find('movename').text, move.find('movebody').text) for move in career_node.find('moves').findall('move')],
                   history=[event.text for event in career_node.find('history').findall('event')],
                   full_text=content(career_node)
                  )
                  
  def __init__(self, name, stats, description, recovery, move_instructions, moves, history, full_text):
    self.__name__ = name
    self.__stats__ = stats
    self.__description__ = description
    self.__recovery__ = recovery
    self.__move_instructions__ = move_instructions
    self.__moves__ = moves
    self.__history__ = history
    self.__full_text__ = full_text
    
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
    
  def getFullText(self):
    return self.__full_text__

class Option(object):
  
  def __init__(self, question, answers):
    self.__question__ = question
    self.__answers__ = answers
    
  def getQuestion(self):
    return self.__question__
    
  def getAnswers(self):
    return self.__answers__

class Setup(object):
  
  @staticmethod
  def fromFile(file_name):
    tree = ET.parse(file_name)
    for setup_node in tree.getroot().iter('setup'):
      yield Setup(title=setup_node.find('title').text,
                  description=setup_node.find('description').text,
                  options=[Option(option.find('question').text, [answer.text for answer in option.iter('li')]) for option in setup_node.find('options').findall('option')],
                  connections=[connection.text for connection in setup_node.find('connections').findall('connection')],
                  full_text=content(setup_node))
  
  def __init__(self, title, description, options, connections, full_text):
    self.__title__ = title
    self.__description__ = description
    self.__options__ = options
    self.__connections__ = connections
    self.__full_text__ = full_text
    
  def getTitle(self):
    return self.__title__
    
  def getDescription(self):
    return self.__description__
    
  def getOptions(self):
    return self.__options__
    
  def getConnections(self):
    return self.__connections__
    
  def getFullText(self):
    return self.__full_text__
    
class BasicMoveList(object):
  def __init__(self, key, title, file_names):
    self.__key__ = key
    self.__title__ = title
    self.__file_names__ = file_names

  def getTitle(self):
    return self.__title__

  def getKey(self):
    return self.__key__

  def getMoves(self):
    if not hasattr(self, '__moves__'):
      self.__moves__ = []
      for filename in self.__file_names__:
        for move in BasicMove.fromFile(filename):
          self.__moves__.append(move)
    return self.__moves__

class BasicMove(object):
  
  @staticmethod
  def fromFile(file_name):
    tree = ET.parse(file_name)
    for move_node in tree.getroot().iter('basicmove'):
      yield BasicMove(name=move_node.find('name').text,
                      normalversion=content(move_node.find('normalversion')),
                      woundedversions=[content(wounded) for wounded in move_node.iter('woundedversion')])
                      
  def __init__(self, name, normalversion, woundedversions):
    self.__name__ = name
    self.__normalversion__ = normalversion
    self.__woundedversions__ = woundedversions
    
  def getName(self):
    return self.__name__
    
  def getNormal(self):
    return self.__normalversion__
    
  def getWoundedVersions(self):
    return self.__woundedversions__
    
  def getWoundedVersionsPairs(self):
    for i in xrange(0, len(self.__woundedversions__), 2):
            yield self.__woundedversions__[i:i+2]