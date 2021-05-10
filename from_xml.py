# -*- coding: utf-8 -*-


import argparse


def find_tag(row: str) -> str:
	a = row.find('<')
	b = row.rfind('<')
	return row[a:-1] if a == b else row[a:b]


def tag_to_object(tag: str):
	if tag == '<list>':
		return []
	elif tag == '<dict>':
		return {}
	elif tag == '<tuple>':
		return ()
	elif tag == '<set>':
		return set()
	else:
		if 'key=' in tag:
			end = tag.find(' t') if 'type=' in tag else tag.find('>')
			return (tag_to_object(tag[tag.find('=') + 1:end]), 
					tag_to_object(tag[tag.find('>') + 1:]))
		elif 'type=str' in tag:
			return tag[tag.find('>') + 1:]
		else:
			elem = tag[tag.find('>') + 1:]
			if ('.' in elem and len(a := elem.split('.')) == 2 
				and a[0].isdigit() and a[1].isdigit()):
				return float(elem)
			elif elem.isdigit():
				return int(elem)
			else:
				return elem


def from_xml(file: str):
	result = [[]]
	row = file.readline()
	row = file.readline()
	while row:
		tag = find_tag(row)
		level = row.find('<')
		if level == 0:
			if tag == '</dict>':	
				return {a: b for a, b in result[0]}
			elif tag == '</tuple>':
				return tuple(result[0])
			elif tag == '</set>':
				return {x for x in result[0]}
			else:
				return result[0]
		if tag[1] == '/':
			temp = result[level - 1][-1]
			if isinstance(temp, tuple):
				temp = tuple([x for x in temp if x != ''] + result[level])
			elif isinstance(temp, dict):
				temp = {a: b for a, b in result[level]}
			elif isinstance(temp, set):
				temp = {x for x in result[level]}
			else:
				temp = [elem for elem in result[level]]
			result[level - 1][-1], result[level] = temp, []
		else:
			obj = tag_to_object(tag)
			result[level - 1].append(obj)
		result.append([])
		row = file.readline()


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-f','--file', default='', help='Name of the file')
	args = parser.parse_args()
	if args.file:
		with open(args.file, 'r') as file:
			print(from_xml(file))
	else:
		f = input('Enter name or path to the file your xml in ')
		with open(f, 'r') as file:
			print(from_xml(file))
