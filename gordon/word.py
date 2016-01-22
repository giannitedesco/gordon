from immutable import ImmutableObject
from operator import itemgetter

class Word(ImmutableObject):
	_fields = ('ko', 'en', 'defn')
	ko = property(itemgetter(0))
	en = property(itemgetter(1))
	defn = property(itemgetter(2))
