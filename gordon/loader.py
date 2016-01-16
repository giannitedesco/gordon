from word import Word
import csv

def load_from_csv(fn):
	out = []
	with open(fn, 'rb') as f:
		r = csv.reader(f)
		for row in r:
			try:
				out.append(Word(*row))
			except TypeError:
				print 'Error on %s:%d'%(fn, r.line_num)
				continue
	return out
