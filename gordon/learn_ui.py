from gi.repository import Gtk
import random

class LearnUI(Gtk.Box):
	def set_kr(self, s):
		self.kr.set_markup('<span size="50000"><b>%s</b></span>'%s)
	def set_en(self, s):
		self.en.set_markup('<span size="30000"><b>%s</b></span>'%s)
	def set_defn(self, s):
		self.defn.set_markup('<span size="20000"><b>%s</b></span>'%s)
	
	def update_word(self, word):
		self.set_kr(word.ko)
		self.set_en(word.en)
		if word.defn is not None:
			self.set_defn(word.defn)
		else:
			self.set_defn('')

	def reshuffle(self):
		self.__shuff = random.sample(self.words, len(self.words))

	def new_word(self):
		if not self.__shuff:
			self.reshuffle()

		self.update_word(self.__shuff.pop())

	def kb_space(self):
		self.new_word()

	def __init__(self, words):
		super(LearnUI, self).__init__(\
				orientation = Gtk.Orientation.VERTICAL,
				spacing = 6)
		self.words = words
		self.reshuffle()

		self.kr = Gtk.Label()
		self.pack_start(self.kr, True, True, 0)

		self.en = Gtk.Label()
		self.pack_start(self.en, True, True, 0)

		self.defn = Gtk.Label()
		self.pack_start(self.defn, True, True, 0)

		self.new_word()

