
from ..parse import Lexer, parse

def test_lexing():

	tokens = lambda x: list(Lexer(x))

	# test basic lambda
	assert tokens('\\x:x') == ['\\', 'x', ':', 'x']

	# multple arguments
	assert tokens('\\x y:x') == [
		'\\', 'x', 'y', ':', 'x'
	]

	# lambda chain
	assert tokens('\\x:\\y:x') == [
		'\\', 'x', ':', '\\', 'y', ':', 'x'
	]

	# parenthesis
	assert tokens('\\x y p: p (x y)') == [
		'\\', 'x', 'y', 'p', ':', 'p', '(', 'x', 'y', ')'
	]

def test_parsing():

	# test basic lambda
	assert parse('\\x:x') == ('lambda', ['x'], ('symbol', 'x'))

	# multple arguments
	assert parse('\\x y:x') == ('lambda', ['x', 'y'], ('symbol', 'x'))

	# lambda chain
	assert parse('\\x:\\y:x') == ('lambda', ['x'], ('lambda', ['y'], ('symbol', 'x')))

	# nested expression
	assert parse('\\x y p:p (x y)') == \
		('lambda', ['x', 'y', 'p'], [('symbol', 'p'), [('symbol', 'x'), ('symbol', 'y')]])

	# nested lambda
	assert parse('\\a:(\\t:t a) a') == \
		('lambda', ['a'], [('lambda', ['t'], [('symbol', 't'), ('symbol', 'a')]), ('symbol', 'a')])

	assert parse('x ((y  z) a) (b c)') == \
		[('symbol', 'x'), [[('symbol', 'y'), ('symbol', 'z')], ('symbol', 'a')], [('symbol', 'b'), ('symbol', 'c')]]
