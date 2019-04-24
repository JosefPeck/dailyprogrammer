#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""[2019-04-08] Challenge #377 [Easy] Axis-aligned crate packing
by Cosmologicon

https://old.reddit.com/r/dailyprogrammer/comments/bazy5j/20190408_challenge_377_easy_axisaligned_crate/
"""


def fit1(X: int, Y: int, x: int, y: int) -> int:
	x_boxes = X // x
	y_boxes = Y // y
	return x_boxes * y_boxes


def fit2(X: int, Y: int, x: int, y: int) -> int:
	return max(
		fit1(X, Y, x, y),
		fit1(X, Y, y, x)
	)


def fit3(
	X: int, Y: int, Z: int, x: int, y: int, z: int, rotated_already: bool = False
) -> int:
	# Doesn't seem to work. TODO.
	rot_list_box: tuple = (X, Y, Z)
	rot_list: tuple = (x, y, z)
	rotation_index = 0
	results = []
	for i in range(3):
		x_boxes = rot_list_box[rotation_index % len(rot_list_box)] // \
			rot_list[rotation_index % len(rot_list)]
		y_boxes = rot_list_box[(rotation_index + 1) % len(rot_list_box)] // \
			rot_list[(rotation_index + 1) % len(rot_list)]
		z_boxes = rot_list_box[(rotation_index + 2) % len(rot_list_box)] // \
			rot_list[(rotation_index + 2) % len(rot_list)]
		results.append(
			x_boxes * y_boxes * z_boxes
		)
		rotation_index += 1
	return max(results)


def main():
	for test in (
		((25, 18, 6, 5), 12),
		((10, 10, 1, 1), 100),
		((12, 34, 5, 6), 10),
		((12345, 678910, 1112, 1314), 5676),
		((5, 100, 6, 1), 0)
	):
		assert fit1(*test[0]) == test[1]
	del test

	for test in (
		((25, 18, 6, 5), 15),
		((12, 34, 5, 6), 12),
		((12345, 678910, 1112, 1314), 5676),
		((5, 5, 3, 2), 2),
		((5, 100, 6, 1), 80),
		((5, 5, 6, 1), 0)
	):
		assert fit2(*test[0]) == test[1]
	del test

	for test in (
		((10, 10, 10, 1, 1, 1), 1000),
		((12, 34, 56, 7, 8, 9), 32),
		((123, 456, 789, 10, 11, 12), 32604),
		((1234567, 89101112, 13141516, 171819, 202122, 232425), 174648)
	):
		pass
		# assert fit3(*test[0]) == test[1]
	del test

	for test in (
		# Lists instead of tuples to be more readable.
		(([3, 4], [1, 2]), 6),
		(([123, 456, 789], [10, 11, 12]), 32604),
		(([123, 456, 789, 1011, 1213, 1415], [16, 17, 18, 19, 20, 21]), 1883443968),
		(
			(
				[
					180598, 125683, 146932, 158296, 171997, 204683, 193694, 216231, 177673,
					169317, 216456, 220003, 165939, 205613, 152779, 177216, 128838, 126894,
					210076, 148407],
				[
					1984, 2122, 1760, 2059, 1278, 2017, 1443, 2223, 2169, 1502, 1274, 1740,
					1740, 1768, 1295, 1916, 2249, 2036, 1886, 2010
				]
			),
			4281855455197643306306491981973422080000
		)
	):
		pass
		# assert fitn(*test[0]) == test[1]
	del test


if __name__ == '__main__':
	main()
