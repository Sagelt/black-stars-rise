from book import Book, Chapter, Setting

jinja_environment = None

default_part_key = 'introduction'
parts = Book([
  Chapter(key='introduction', title='Introduction', file_name='text/introduction.xml'),
  Setting(key='smalltown', title='Small Town', file_names=[
                                    'text/careers/doctor.xml',
                                    'text/careers/reporter.xml',
                                    'text/careers/librarian.xml',
                                    'text/careers/detective.xml',
                                    'text/careers/professor.xml',
                                    'text/careers/mechanic.xml',
                                    'text/careers/priest.xml',
                                    'text/careers/artist.xml',
                                    'text/setups/the-mansion-on-the-hill.xml',
  ])
])