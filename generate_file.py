# -*- coding: utf-8 -*-

import random
import sys
import argparse


symbols_dict = {
	'latin': (97, 122),
	'digits': (48, 57),
	'cyrilic': (1072, 1105)
}


def generate_lines(size: float, symbols: str, line: tuple, word: tuple):
	size_left = int(size * 1024 ** 2)
	progress_bar = str(input('Do you want to see progress bar (yes or no)? '))
	while size_left > 0:
		words = []
		for num in range(random.randint(*line)):
			word_len = random.randint(*word)
			cur_word = ''.join([chr(random.randint(*symbols_dict[symbols])) for _ in range(word_len)])
			words.append(cur_word)
		cur_line = (" ".join(words) + "\n").encode('utf-8')
		cur_line = cur_line[:size_left]
		yield cur_line
		size_left -= len(cur_line)
		if progress_bar == 'yes':
			status = (1 - size_left/int(size * 1024 ** 2)) * 100
			sys.stdout.write('\r')
			sys.stdout.write("[%-100s] %d%%" % ('~' * int(status),   status))
			sys.stdout.flush()


def generate_file(size: float, symbols: str, line: tuple, word: tuple, file: str):
	with open(file, 'wb') as f:
		f.writelines(generate_lines(size, symbols, line, word))


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'Size, symbols, number of words in line and length of words')
	parser.add_argument('-s','--size', default=1, type=float, help='The size of the file')
	parser.add_argument('-t','--symbols', default='latin', type=str, choices=['latin','digits','cyrilic'], help='The type of symbols')
	parser.add_argument('-l','--line', default=(10, 50), help='The number of words in line (one integer or two integers separated by comma)')
	parser.add_argument('-w','--word', default=(5, 9), help='The length of words (one integer or two integers separated by comma)')
	args = parser.parse_args()
	if not isinstance(args.line, tuple):
		if len(args.line) == 1:
			args.line = tuple([int(args.line[0]), int(args.line[0])])
		else:
			args.line = tuple([int(args.line[0]), int(args.line[2])])
	if not isinstance(args.word, tuple):
		if len(args.word) == 1:
			args.word = tuple([int(args.word[0]), int(args.word[0])])
		else:
			args.word = tuple([int(args.word[0]), int(args.word[2])])
	file = str(input('Input file name or path to the file '))
	generate_file(args.size, args.symbols, args.line, args.word, file)
