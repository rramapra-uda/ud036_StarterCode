'''
Created on 19-Jul-2017

@author: rramapra
'''

import media
from fresh_tomatoes import open_movies_page


dangal = media.Movie(title='Dangal',\
                        poster_url="https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg",\
                            trailer_url="https://www.youtube.com/watch?v=x_7YlGv9u1g")

bahubali_begin = media.Movie(title="Bahubali The Beginning", \
                            poster_url="http://static.dnaindia.com/sites/default/files/2015/05/02/332842-baahubali.jpg", \
                                trailer_url="https://www.youtube.com/watch?v=3NQRhE772b0")

bahubali_conclusion = media.Movie(title="Bahubali The Conclusion", \
                            poster_url="http://static.koimoi.com/wp-content/new-galleries/2017/01/bahubali-the-conclusion-presenting-amarendra-baahubali-devasena-1.jpg", \
                                trailer_url="https://www.youtube.com/watch?v=G62HrubdD6o")

movies = list([dangal, bahubali_begin, bahubali_conclusion])

open_movies_page(movies)
