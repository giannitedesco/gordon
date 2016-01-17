class ImmutableObject(tuple):
	"Abstrace base class for immutable objects"

	__slots__ = ()
	def __new__(_cls, *args, **kwargs):
		if kwargs:
			t = tuple(map(lambda x: kwargs.pop(x, None),
				_cls._fields))
			if kwargs:
				raise Exception('Unknown fields: %s'%\
						', '.join(kwargs.keys()))
		else:
			t = args + tuple([None for x in
				xrange(len(_cls._fields) - len(args))])
		return tuple.__new__(_cls, t)
	def __repr__(self):
		s = map(lambda (k,v):'%s=%s'%(k,v),
			zip(self._fields, self))
		return self.__class__.__name__ + '(%s)'%', '.join(s)
