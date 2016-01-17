from gi.repository import Gtk
import random

from verb import Verb
from noun import Noun

class TestUI(Gtk.Box):
	def set_q(self, s):
		self.q.set_markup('<span size="50000"><b>%s</b></span>'%s)
	
	def __press(self, b):
		if b.is_correct:
			self.new_word()
		else:
			# TODO: something
			pass

	def get_answers(self, word):
		a = set()
		if isinstance(word, Verb):
			srch = self.kr_v
		elif isinstance(word, Noun):
			srch = self.kr_n
		else:
			srch = self.kr_words

		while(len(a) != 3):
			a.update(random.sample(srch, 3 - len(a)))
			if word in a:
				a.remove(word)
				continue

		assert len(set(a | set({word}))) == 4
		a = [(word.ko, True)] + [(x, False) for x in list(a)]
		random.shuffle(a)
		return a

	def update_word(self, word):
		self.set_q(word.en)
		a = self.get_answers(word)

		for i, (a, is_correct) in enumerate(a):
			self.b[i].get_child().set_markup_with_mnemonic(\
				'<span size="30000"><b>_%d. %s</b></span>'%\
					(i + 1, a))
			self.b[i].is_correct = is_correct

	def reshuffle(self):
		self.__shuff = random.sample(self.words, len(self.words))

	def new_word(self):
		if not self.__shuff:
			self.reshuffle()

		self.update_word(self.__shuff.pop())

	def kb_space(self):
		return

	def __init__(self, words):
		super(TestUI, self).__init__(\
				orientation = Gtk.Orientation.VERTICAL,
				spacing = 6)

		self.kr_words = [x.ko for x in words]
		self.en_words = [x.en for x in words]
		self.kr_v = [x.ko for x in words \
				if isinstance(x, Verb)]
		self.kr_n = [x.ko for x in words \
				if isinstance(x, Noun)]
		self.words = words
		self.reshuffle()

		self.q = Gtk.Label()
		self.pack_start(self.q, True, True, 0)

		table = Gtk.Table(2, 2, True)

		self.b = []
		for i in xrange(4):
			b = Gtk.Button(label = '%d'%(i + 1))
			b.connect('clicked', self.__press)
			b.props.focus_on_click = False
			self.b.append(b)

		table.attach(self.b[0], 0, 1, 0, 1)
		table.attach(self.b[1], 1, 2, 0, 1)
		table.attach(self.b[2], 0, 1, 1, 2)
		table.attach(self.b[3], 1, 2, 1, 2)

		self.pack_start(table, True, True, 0)

		self.new_word()
