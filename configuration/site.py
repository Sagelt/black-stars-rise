from book import Book, SingleFileSection, Setting

jinja_environment = None

default_section_key = 'Introduction'
sections = Book([
  SingleFileSection(key='introduction', title='Introduction', file_name='text/introduction.xml'),
  Setting(key='smalltown', title='Small Town', file_names=[
                                    'text/careers/basic.xml',
  ])
])