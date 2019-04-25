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

	WIRE_STRINGS: List[str] = [
		'WHITE',
		'RED',
		'BLACK',
		'ORANGE',
		'GREEN',
		'PURPLE'
	]


class Bomb:

	UNKNOWN: int = 0
	DEFUSED: int = 1
	EXPLODED: int = 2

	STATUS_STRINGS: List[str] = [
		'UNKNOWN',
		'DEFUSED',
		'EXPLODED'
	]

	status = 0

	must_cut: set = set()
	can_not_cut: set = set()

	wires_cut: int = 0

	def cut(self, wire):
		print('Step {}: Cutting wire {}'.format(
			self.wires_cut + 1, Wire.WIRE_STRINGS[wire]
		))

		if wire in self.can_not_cut:
			print(
				'Explode: wire {} must not be any of {}'.format(
					Wire.WIRE_STRINGS[wire],
					', '.join([
						Wire.WIRE_STRINGS[i] for i, _ in enumerate(
							self.can_not_cut
						)
					])
				)
			)
			self.explode()
		else:
			self.can_not_cut = set()

		if len(self.must_cut) > 0:
			if wire not in self.must_cut:
				self.explode()
			else:
				self.must_cut = set()

		if wire == Wire.WHITE:
			print('Next step: Can not cut WHITE or BLACK.')
			self.can_not_cut = {Wire.WHITE, Wire.BLACK}

		elif wire == Wire.RED:
			print('Next step: Must cut GREEN.')
			self.must_cut = {Wire.GREEN}

		elif wire == Wire.BLACK:
			# if Wire.WHITE in self.cut_wires or Wire.GREEN in self.cut_wires \
			# 	or Wire.ORANGE in self.cut_wires:
			# 	self.explode()
			print('Next step: Can not cut WHITE, GREEN, ORANGE.')
			self.can_not_cut = {Wire.WHITE, Wire.GREEN, Wire.ORANGE}

		elif wire == Wire.ORANGE:
			print('Next step: Must cut RED or BLACK.')
			self.must_cut = {Wire.RED, Wire.BLACK}

		elif wire == Wire.GREEN:
			print('Next step: Must cut ORANGE or WHITE.')
			self.must_cut = {Wire.ORANGE, Wire.WHITE}

		elif wire == Wire.PURPLE:
			print('Next step: Can not cut PURPLE, GREEN, ORANGE, WHITE.')
			self.can_not_cut = {Wire.PURPLE, Wire.GREEN, Wire.ORANGE, Wire.WHITE}

		self.wires_cut += 1

	def explode(self):
		self.status = Bomb.EXPLODED


def main():
	for test in (
		(
			(),
			Bomb.UNKNOWN
		),
		(
			(
				Wire.WHITE,
				Wire.RED,
				Wire.GREEN,
				Wire.WHITE
			),
			Bomb.DEFUSED
		),
		(
			(
				Wire.WHITE,
				Wire.ORANGE,
				Wire.GREEN,
				Wire.WHITE
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
