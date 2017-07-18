'''
Created on 19-Jul-2017

@author: rramapra
'''

class Movie(object):
    '''
    class to hold information about a movie
    '''


    def __init__(self, title, poster_url, trailer_url):
        '''
        @input: title, poster_url, trailer_url 
        @description: constructor for Movie class
        '''
        self.title = title
        self.poster_url = poster_url
        self.trailer_url = trailer_url
    
    def __repr__(self):
        '''
        @output: string representation of object
        @description: function that gives a string representation of the Movie object
        '''
        return "Movie(title={}, poster={}, trailer={})".format(self.title, self.poster_url, self.trailer_url)
    
    @property
    def poster_image_url(self):
        return self.poster_url
    
    @property
    def trailer_youtube_url(self):
        return self.trailer_url
    
    