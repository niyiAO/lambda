
class Enviroment(dict):
	
	def __init__(self, bnds=None, par=None):

		if not bnds is None:
			super(Enviroment, self).__init__(bnds)

		self._parent = par

	def get(self, sym):
		v = super(Enviroment, self).get(sym)

		if not v and self._parent:
			return self._parent.get(sym)

		return v

	def push(self, bnds=None):
		return Enviroment(bnds, self)
