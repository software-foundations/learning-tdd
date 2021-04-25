from typing import Callable, Sequence, Iterable

def return_function(function: Callable[[], None]) -> Callable:
	return function


def say_hello():
	print('Hello')


return_function(function=say_hello)


def my_sum(x: int, y: int) -> int:
	return x + y


def return_function2(function: Callable[[int, int], int]) -> Callable:
	return function

result = return_function2(my_sum)(10, 20)
print(result)

def iterate(sequence: Sequence[int]):
	return [x * 2 for x in sequence]

def iterate2(sequence: Iterable[int]):
	return [x * 2 for x in sequence]

print(iterate([1, 2, 3]))
print(iterate((1, 2, 3)))

print(iterate2([1, 2, 3]))
print(iterate2((1, 2, 3)))