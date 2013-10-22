#!/usr/bin/env python
import configuration.setup
import jinja2
import webapp2
import os

configuration.setup.jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 
                                 "templates")))

class PartHandler(webapp2.RequestHandler):
    def get(self, part_key=None):
      if not part_key:
        part_key = configuration.setup.parts.getDefaultPartKey()
      
      template_values = dict()
      part = configuration.setup.parts.getPartByKey(part_key)
      if hasattr(part, 'getSections'):
        template_values['sections'] = part.getSections()
      elif hasattr(part, 'getCareers'):
        template_values['career_names'] = part.getCareerNames()
        template_values['careers'] = part.getCareers()
        template_values['setup_titles'] = part.getSetupTitles()
        template_values['setups'] = part.getSetups()
      template_values['parts'] = configuration.setup.parts.getParts()
      template_values['current'] = part_key
      
      template = configuration.setup.jinja_environment.get_template('chapter.html')
      self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    webapp2.Route(
      r'/part/<part_key:[\d\w%]+>', 
      handler=PartHandler, 
      name='part'),
    webapp2.Route(
      r'/', 
      handler=PartHandler, 
      name='home'),
], debug=True)
