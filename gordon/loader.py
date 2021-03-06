from noun import Noun
from verb import Verb
from word import Word

def load_from_csv(fn):
	out = []
	gd = {
		'Noun': Noun,
		'Verb': Verb,
		'Word': Word,
	}
	ld = {}
	with open(fn, 'rb') as f:
		line_num = 1
		for l in iter(f.readline, ''):
			try:
				x = eval(l.rstrip('\r\n'), ld, gd)
			except Exception as e:
				print '%s:%d: %s'%(fn, line_num, e.message)
			out.append(x)
			line_num += 1
	return out
