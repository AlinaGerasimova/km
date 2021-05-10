# -*- coding: utf-8 -*-


import sys


def get_fib(n: int) -> int:
	a, b = 0, 1
	if n == 0:
		return a
	else:
		while n > 1:
			a, b = b, a+b
			n -= 1
		return b


if __name__ == '__main__':
	try:
		if len(sys.argv) > 1:
			print(get_fib(int(sys.argv[1])))
		else:
			n = input('Input the index of Fibonacci number ')
			print(get_fib(int(n)))
	except ValueError:
		print('Input Error!')
