from book import Book, Chapter, Setting

jinja_environment = None

default_part_key = 'introduction'
parts = Book([
  Chapter(key='introduction', title='Introduction', file_name='text/introduction.xml'),
  Setting(key='smalltown', title='Small Town', file_names=[
                                    'text/careers/basic.xml',
  ])
])