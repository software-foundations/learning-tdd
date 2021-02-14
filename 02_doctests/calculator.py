def sum(x, y):
	"""Sum x and y

	>>> sum(10, 20)
	30

	>>> sum(-10, 20)
	10

	>>> sum('10', 20)
	Traceback (most recent call last):
	...
	AssertionError: x needs to be in or float
	"""

	assert isinstance(x, (int, float)), 'x needs to be in or float'
	assert isinstance(y, (int, float)), 'x needs to be in or float'

	return x + y

def subtract(x, y):
	"""Subtract x and y

	>>> subtract(10, 5)
	5

	>>> subtract('10', 5)
	Traceback (most recent call last):
	...
	TypeError: unsupported operand type(s) for -: 'str' and 'int'
	"""	
	return x - y

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True)
