from book import Book, SingleFileSection, CareerSection

jinja_environment = None

default_section_key = 'Introduction'
sections = Book([
  SingleFileSection(title='Introduction', file_name='text/introduction.xml'),
  CareerSection(title='Careers', file_names=[
                                    'text/careers/doctor.xml',
  ])
])