#!/usr/bin/env python
from configuration.setup import black_stars_rise
import jinja2
import webapp2
import os

jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 
                                 "templates")))

class PartHandler(webapp2.RequestHandler):
    def get(self, part_key=None):
      if not part_key:
        part_key = black_stars_rise.getDefaultPartKey()
      
      template_values = dict()
      part = black_stars_rise.getPartByKey(part_key)
      if hasattr(part, 'getSections'):
        template_values['sections'] = part.getSections()
      elif hasattr(part, 'getCareers'):
        template_values['career_names'] = part.getCareerNames()
        template_values['careers'] = part.getCareers()
        template_values['setup_titles'] = part.getSetupTitles()
        template_values['setups'] = part.getSetups()
      template_values['parts'] = black_stars_rise.getParts()
      template_values['current'] = part_key
      
      template = jinja_environment.get_template('chapter.html')
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
