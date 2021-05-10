# -*- coding: utf-8 -*-


def flatten_it(obj):
	if isinstance(obj, dict):
		flatten_dict = []
		for k, v in obj.items():
			if v == obj:
				raise ValueError
			flatten_dict.extend((k, v))
		yield from flatten_it(flatten_dict)
	elif hasattr(obj, '__iter__') and not isinstance(obj, str):
		for elem in obj:
			if elem == obj:
				raise ValueError
			else:
				yield from flatten_it(elem)
	else:
		yield obj


if __name__ == '__main__':
	test_1 = [1, [2, [345, 4, {'a': (2, 2), 5: 'abc'}, 'abcdef', []]]]
	print(test_1, '->', list(flatten_it(test_1)))
	test = [1, 1]
	test[1] = test
	test_2 = [[1, 2], {'345': test, 2: 3}]
	try: 
		print(test_2, '->', list(flatten_it(test_2)))
	except ValueError:
		print('Cyclic reference')
