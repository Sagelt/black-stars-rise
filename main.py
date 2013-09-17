#!/usr/bin/env python
import configuration.site
import jinja2
import webapp2
import os

configuration.site.jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 
                                 "templates")))

class SectionHandler(webapp2.RequestHandler):
    def get(self, section_key=None):
      if not section_key:
        section_key = configuration.site.default_section_key
      
      template_values = dict()
      section = configuration.site.sections.getSectionByTitle(section_key)
      if hasattr(section, 'getText'):
        template_values['text'] = section.getText()
      elif hasattr(section, 'getCareers'):
        template_values['careers'] = section.getCareers()
      template_values['sections'] = configuration.site.sections.getSectionTitles()
      template_values['current'] = section_key
      
      template = configuration.site.jinja_environment.get_template('chapter.html')
      self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    webapp2.Route(
      r'/section/<section_key:[\d\w%]+>', 
      handler=SectionHandler, 
      name='section'),
    webapp2.Route(
      r'/', 
      handler=SectionHandler, 
      name='home'),
], debug=True)
