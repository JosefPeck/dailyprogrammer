#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""
https://old.reddit.com/r/dailyprogrammer/comments/a0lhxx/20181126_challenge_369_easy_hex_colors/
"""


def hexcolor(r: int, g: int, b: int) -> str:
	return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def hex_to_rgb(hex_string: str) -> tuple:
	hex_no_sharp = hex_string
	if hex_string[:1] == '#':
		hex_no_sharp = hex_string[1:]
	rgb = []
	for i in range(0, 6, 2):
		rgb.append(
			int(hex_no_sharp[i:i + 2])
		)
	return tuple(rgb)


def blend(colors: set) -> str:
	r_list: list = []
	g_list: list = []
	b_list: list = []
	for color in colors:
		rgb_color = hex_to_rgb(color)
		r_list.append(rgb_color[0])
		g_list.append(rgb_color[1])
		b_list.append(rgb_color[2])
	r = sum(r_list) // len(r_list)
	g = sum(g_list) // len(g_list)
	b = sum(b_list) // len(b_list)
	print(hexcolor(r, g, b))
	return hexcolor(r, g, b)


def main():
	# hexcolor(255, 99, 71) => "#FF6347"  (Tomato)
	# hexcolor(184, 134, 11) => "#B8860B"  (DarkGoldenrod)
	# hexcolor(189, 183, 107) => "#BDB76B"  (DarkKhaki)
	# hexcolor(0, 0, 205) => "#0000CD"  (MediumBlue)
	for test in (
		((255, 99, 71), '#FF6347'),
		((184, 134, 11), '#B8860B'),
		((189, 183, 107), '#BDB76B'),
		((0, 0, 205), '#0000CD')
	):
		# Returns lowercase characters, so need lower()
		assert hexcolor(*test[0]) == test[1].lower()
	del test

	for test in (
		({"#000000", "#778899"}, '#3C444C'),
	):
		pass  # TODO
		# assert blend(test[0]) == test[1].lower()


if __name__ == '__main__':
	main()
