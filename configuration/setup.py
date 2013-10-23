from book import Book, Chapter, Setting, BasicMoveList

black_stars_rise = Book([
  Chapter(key='introduction', title='Introduction', file_name='text/introduction.xml'),
  BasicMoveList(key='basicmoves', title='Basic Moves', file_names=[
                                    'text/basic_moves/take-a-risk.xml',
                                    'text/basic_moves/suffer-harm.xml',
                                    'text/basic_moves/keep-it-together.xml',
                                    'text/basic_moves/study.xml',
  ]),
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
  ]),
])