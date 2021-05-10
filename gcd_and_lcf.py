# -*- coding: utf-8 -*-

def find_gcd(a: int, b: int) -> int:
	a, b = max(a, b), min(a, b)
	while b != 0:
		a, b = b, a % b
	return a


def find_lcf(a: int, b: int) -> int:
	return a * b // find_gcd(a, b)


if __name__ == '__main__':
	num1, num2 = input('Enter two numbers ').split(' ')
	try: 
		print(find_gcd(int(num1), int(num2)), find_lcf(int(num1), int(num2)))
	except ValueError:
		print('Input Error')