from word import Word
from operator import itemgetter

class Noun(Word):
	_fields = ('ko', 'en', 'defn')
	ko = property(itemgetter(0))
	en = property(itemgetter(1))
	defn = property(itemgetter(2))
