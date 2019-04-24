#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""320 [Easy] Spiral Ascension
https://old.reddit.com/r/dailyprogrammer/comments/6i60lr/20170619_challenge_320_easy_spiral_ascension/
"""


def spiral(start: int) -> list:  # TODO
	list_length: int = start
	# First, let's create a multidimensional list.
	total_list: list = [
		[
			None for z in range(list_length)
		] for i in range(list_length)
	]

	# Great, now we start at the beginning.
	total_items: int = sum(len(item) for item in total_list)
	for a in range(total_items):


	return total_list


def main():
	for test in (
		(5, []),
	):
		assert spiral(test[0]) == test[1]


if __name__ == '__main__':
	main()
