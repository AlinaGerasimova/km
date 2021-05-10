# -*- coding: utf-8 -*-


import argparse


def to_xml(obj, indent: str = '') -> str:
	result = ''
	if hasattr(obj, "__iter__") and not isinstance(obj, str):
		if isinstance(obj, dict):
			result += indent + '<dict>\n'
			for k, v in obj.items():
				if hasattr(v, "__iter__") and not isinstance(v, str):
					elem = to_xml(v, indent + '  ')
					result += f'{indent} <item key={k}>\n{elem}{indent} </item>\n'
				elif isinstance(v, str) and v.isdigit():
					result += indent + ' ' + f"<item key={k} type='str'>{v}</item>\n"
				else:
					result += indent + ' ' + f'<item key={k}>{v}</item>\n'
			result += indent + '</dict>\n'
		else:
			name = str(type(obj))[8:-2]
			result += indent + f'<{name}>\n'
			for elem in obj:
				if hasattr(elem, "__iter__") and not isinstance(elem, str):
					result += to_xml(elem, indent + ' ')
				elif isinstance(elem, str) and elem.isdigit():
					result += indent + ' ' + f"<item type='str'>{elem}</item>\n"
				else:
					result += indent + ' ' + f'<item>{elem}</item>\n'
			result += indent + f'</{name}>\n'	
	else:
		return f'<item>{obj}</item>'
	return result


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'Name or path to the file you want to save your xml in')
	parser.add_argument('-f','--file', default='', help='Name of the file')
	args = parser.parse_args()
	test = '1'
	if args.file:
		with open(args.file, 'w') as file:
			file.write(to_xml(test))
	else:
		f = input('Enter name or path to the file you want to save your xml in ')
		with open(f, 'w') as file:
			file.write(to_xml(test))
