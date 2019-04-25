#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""293 [Easy] Defusing the bomb
https://old.reddit.com/r/dailyprogrammer/comments/5e4mde/20161121_challenge_293_easy_defusing_the_bomb/
"""

from typing import List


class Wire:
	WHITE: int = 0
	RED: int = 1
	BLACK: int = 2
	ORANGE: int = 3
	GREEN: int = 4
	PURPLE: int = 5

	id_of: int = -1
	# Allow any by default.
	allowed: tuple = (0, 1, 2, 3, 4, 5)


class WireWhite(Wire):
	name: str = "WHITE"
	id_of: int = 0
	allowed: tuple = (
		Wire.RED,
		Wire.ORANGE,
		Wire.GREEN,
		Wire.PURPLE
	)


class WireRed(Wire):
	name: str = "RED"
	id_of: int = 1
	allowed: tuple = (
		Wire.GREEN,
	)


class WireBlack(Wire):
	name: str = "BLACK"
	id_of: int = 2
	allowed: tuple = (
		Wire.RED,
		Wire.BLACK,
		Wire.PURPLE
	)


class WireOrange(Wire):
	name: str = "ORANGE"
	id_of: int = 3
	allowed: tuple = (
		Wire.RED,
		Wire.BLACK
	)


class WireGreen(Wire):
	name: str = "GREEN"
	id_of: int = 4
	allowed: tuple = (
		Wire.WHITE,
		Wire.ORANGE
	)


class WirePurple(Wire):
	name: str = "PURPLE"
	id_of: int = 5
	allowed: tuple = (
		Wire.RED,
		Wire.BLACK
	)


class Bomb:

	UNKNOWN: int = 0
	DEFUSED: int = 1
	EXPLODED: int = 2

	# Defused is default, seemingly.
	status = 1

	wires_cut: int = 0

	last_cut: Wire = Wire

	def cut(self, wire):
		print('Step {}: Cutting wire {}'.format(
			self.wires_cut + 1, wire.name
		))

		if wire.id_of not in self.last_cut.allowed:
			self.explode()

		self.last_cut = wire

		self.wires_cut += 1

	def explode(self):
		self.status = Bomb.EXPLODED


def main():
	for test in (
		(
			(),
			Bomb.DEFUSED
		),
		(
			(
				WireWhite,
				WireRed,
				WireGreen,
				WireWhite
			),
			Bomb.DEFUSED
		),
		(
			(
				WireWhite,
				WireOrange,
				WireGreen,
				WireWhite
			),
			Bomb.EXPLODED
		)
	):
		bomb: Bomb = Bomb()
		for direction in test[0]:
			bomb.cut(direction)
		print(test[1], bomb.status, bomb.wires_cut)
		assert test[1] == bomb.status


if __name__ == '__main__':
	main()
