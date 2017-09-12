
import re

class Lexer:

	def __init__(self, src):
		self._src = src

	def __next__(self):

		tokens = [
			r'\s*([()\\;])',
			r'\s*(:)',
			r'\s*([^()\\;:\s]+)',
		]

		for r in tokens:
			m = re.match(r, self._src)
			if m:
				self._src = self._src[m.end():]
				return m.group(1)

		raise StopIteration

	def __iter__(self):
		return self

def parse(text):
	lexer = Lexer(text)
	return parse_exp(lexer, ';')

def parse_exp(lexer, term):

	exps = []

	try:
		while True:
			token = next(lexer)

			if token == '\\':
				internal = parse_lambda(lexer)
				exps.append(internal)
			elif token == '(':
				internal = parse_exp(lexer, ')')
				exps.append(internal)
			elif token is term:
				return exps[0] if len(exps) == 1 else exps
			else:
				exps.append(('symbol', token))

	except StopIteration:
		return exps[0] if len(exps) == 1 else exps

def parse_lambda(lexer):
	token = next(lexer)
	args = []

	while token != ':':
		args.append(token)
		token = next(lexer)

	body = parse_exp(lexer, ')')
	return ('lambda', args, body)

a = parse('\\a:(\\t:t a) a')
# a = parse('x ((y  z) a) (b c)')
print(a)
