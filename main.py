#!/usr/bin/env python
import codecs
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
      text_file = codecs.open(configuration.site.sections[section_key], encoding='utf-8')
      text = text_file.read()
      text_file.close()
      
      template_values = dict()
      template_values['text'] = text
      template_values['sections'] = configuration.site.sections.items()
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
