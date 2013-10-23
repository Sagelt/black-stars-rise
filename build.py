from configuration.setup import black_stars_rise
import shutil
import os
import codecs

if __name__ == '__main__':
  
  # Always build from scratch.
  # We're just doing a little xml parsing, the work in making it incremental
  # just doesn't seem worth it. Instead we invent the universe to make an 
  # apple pie.
  if os.path.isdir('build'):
    shutil.rmtree('build')
  if not os.path.isdir('build'):
    os.mkdir('build')
    
  for part in black_stars_rise.getParts():
    # Check to see if it's a chapter
    if hasattr(part, 'getSections'):
      with codecs.open(os.path.join('build', part.getKey()+'.xml'), 'w', "utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
        f.write('<chapter>')
        for section in part.getSections():
          f.write(section.getText())
          f.write('\n')
        f.write('</chapter>')
    elif hasattr(part, 'getCareers'): # It's a setting
      with codecs.open(os.path.join('build', part.getKey()+'.xml'), 'w', "utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
        f.write('<setting><careers>')
        for career in part.getCareers():
          f.write('<career>')
          f.write(career.getFullText())
          f.write('</career>\n')
        f.write('</careers>\n')
        f.write('<setups>')
        for setup in part.getSetups():
          f.write('<setup>')
          f.write(setup.getFullText())
          f.write('</setup>\n')
        f.write('</setups></setting>')
    elif hasattr(part, 'getMoves'): # It's basic moves
      with codecs.open(os.path.join('build', part.getKey()+'.xml'), 'w', "utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
        f.write('<moves>')
        for move in part.getMoves():
          woundedVersions = move.getWoundedVersions()
          # For now, assume a 9-per-page layout
          for i in xrange(0,9):
            f.write('<basicmovename>')
            f.write(move.getName())
            f.write('</basicmovename>\n')
            f.write('<movebody>')
            f.write(move.getNormal())
            f.write('</movebody>\n')
          for i in xrange(0,9):
            f.write('<basicmovename>')
            f.write(move.getName())
            f.write('</basicmovename>\n')
            f.write('<movebody>')
            f.write(woundedVersions[i % len(woundedVersions)])
            f.write('</movebody>\n')
        f.write('</moves>')
      