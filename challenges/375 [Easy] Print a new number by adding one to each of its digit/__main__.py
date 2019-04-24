#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

# Not the best solution but it works I guess.


def printer(integer: int) -> int:
	assert isinstance(integer, int)
	data = str(integer)
	new = []
	for chara in data:
		new.append(
			str(
				int(
					chara
				) + 1
			)
		)
	return int(''.join(new))


def main():
	for test in (
		(998, 10109),
	):
		assert printer(test[0]) == test[1]
