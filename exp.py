
from env import Enviroment

class Lambda:

	def __init__(self, names, body, parent):
		self.names = names
		self.env = parent
		self.body = body

	def call(self, *args):

		if len(args) > len(self.names):
			raise ValueError

		bnds = {}
		for k, v in zip(self.names, args):
			bnds[k] = v

		if len(self.names) == len(args):
			return eval_exp(self.body, self.env.push(bnds))
		else:
			return Lambda(self.names[len(args):], self.body, self.env.push(bnds))

	def __repr__(self):
		return f"lambda {self.names} -> {self.body}"

def evaluate(exp, env):

	if isinstance(exp, list):

		e = [eval_exp(i, env) for i in exp]
		if isinstance(e[0], Lambda):
			return e[0].call(*e[1:])
		else:
			raise ValueError

	if exp[0] is 'lambda':
		return Lambda(exp[1], exp[2], env)

	if exp[0] is 'symbol':
		return env.get(exp[1])
