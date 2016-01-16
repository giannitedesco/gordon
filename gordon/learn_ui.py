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
		self.set_kr(word.korean)
		self.set_en(word.english)
		self.set_defn(word.definition)
		self.word = word

	def new_word(self):
		while True:
			word = random.choice(self.words)
			if self.word != word:
				break
		self.update_word(word)

	def kb_space(self):
		self.new_word()

	def __init__(self, words):
		super(LearnUI, self).__init__(\
				orientation = Gtk.Orientation.VERTICAL,
				spacing = 6)
		self.words = words
		self.word = None

		self.kr = Gtk.Label()
		self.pack_start(self.kr, True, True, 0)

		self.en = Gtk.Label()
		self.pack_start(self.en, True, True, 0)

		self.defn = Gtk.Label()
		self.pack_start(self.defn, True, True, 0)

		self.new_word()

