# -*- coding: utf-8 -*-


import argparse
import sys


def take_row(file, pos):
	file.seek(pos)
	return file.readline()


def merge_sort(arr: list, key: str = '') -> list:
	if len(arr) >= 2:
		left = merge_sort(arr[:len(arr) // 2], key)
		right = merge_sort(arr[len(arr) // 2:], key)
		res = []
		if key == '':
			while len(left) and len(right):
				if left[0] <= right[0]:
					res.append(left.pop(0))
				else:
					res.append(right.pop(0))
		else:
			while len(left) and len(right):
				row_left = take_row(key, left[0])
				row_right = take_row(key, right[0])
				if row_left <= row_right:
					res.append(left.pop(0))
				else:
					res.append(right.pop(0))
		return res + left + right
	else:
		return arr


def file_sort(file_in: str, file_out: str, progress: str):
	positions = []
	file_tmp = '_tmp.'.join(file_out.rsplit('.', 1))

	print('Sorting words in lines...')
	with open(file_in, 'r') as f_in:
		with open(file_tmp, 'w') as f_tmp:
			pos = 0
			row = f_in.readline()
			while row:
				positions.append(pos)
				pos = f_in.tell()
				f_tmp.write(' '.join(merge_sort(row.split())) + '\n')
				row = f_in.readline()

	print('Sorting lines...')
	with open(file_tmp, 'r') as f_tmp:
		with open(file_out, 'w') as f_out:
			new_positions = merge_sort(positions, f_tmp)
			for i in new_positions:
				f_out.write(take_row(f_tmp, i))
				if progress == 'yes':
					status = (new_positions.index(i) + 1)/len(positions) * 100
					sys.stdout.write('\r')
					sys.stdout.write("[%-100s] %d%%" % ('~' * int(status),   status))
					sys.stdout.flush()


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-f','--file', default='', help='Name or path to the file with text')
	parser.add_argument('-o','--out', default='', help='Name or path to the file to save result in')
	parser.add_argument('-p','--progress', default='', help='Do you want to see progress bar (yes or no)?')
	args = parser.parse_args()
	file_in = args.file if args.file else input('Name of the file with text you want to sort: ')
	file_out = args.out if args.out else input('Name of the file in which you want to save sorted text: ')
	prog = args.progress if args.progress else input('Do you want to see progress bar (yes or no)? ')
	file_sort(file_in, file_out, prog)
