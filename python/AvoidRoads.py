#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://community.topcoder.com/stat?c=problem_statement&pm=1889&rd=4709

from unittest import TestCase, main
import pudb

class AvoidRoads:
	def parse_bad(self, bad):
		new_bad = []

		for elem in bad:
			subelems = elem.split(' ')
			if len(subelems) != 4:
				raise ValueError()

			p1 = (int(subelems[0]), int(subelems[1]))
			p2 = (int(subelems[2]), int(subelems[3]))

			if p1[0] <= p2[0]:
				new_bad.append( (p1, p2) )
			else:
				new_bad.append( (p2, p1) )

		return new_bad


	def numWays(self, width, height, bad):
		#pu.db
		bad = self.parse_bad(bad)
		#print "{0}x{1}: {2}".format(width, height, bad)
		space = [ [ 0 for x in xrange(width + 1) ] for y in xrange(height + 1) ]

		for y in xrange(height + 1):
			for x in xrange(width + 1):
				if x == 0 and y == 0:
					space[y][x] = 1
					continue

				# Inherit left if not in bad
				if ((x-1,y), (x,y)) not in bad and x > 0:
					space[y][x] += space[y][x-1]
				# Inherit bottom if not in bad
				if ((x,y-1), (x,y)) not in bad and y > 0:
					space[y][x] += space[y-1][x]

		return space[height][width]


	def __call__(self, w, h, bad):
		return self.numWays(w, h, bad)


class TestAvoidRoads(TestCase):
	def setUp(self):
		self.inst = AvoidRoads()

	def test_00(self):
		w   = 6
		h   = 6
		bad = [ "0 0 0 1", "6 6 5 6" ]
		exp = 252
		ret = self.inst(w, h, bad)
		self.assertEqual( ret, exp )


	def test_01(self):
		w   = 1
		h   = 1
		bad = [ ]
		exp = 2
		ret = self.inst(w, h, bad)
		self.assertEqual( ret, exp )


	def test_02(self):
		w   = 35
		h   = 31
		bad = [ ]
		exp = 6406484391866534976
		ret = self.inst(w, h, bad)
		self.assertEqual( ret, exp )


	def test_03(self):
		w   = 2
		h   = 2
		bad = [ "0 0 1 0", "1 2 2 2", "1 1 2 1" ]
		exp = 0
		ret = self.inst(w, h, bad)
		self.assertEqual( ret, exp )


if __name__ == '__main__':
	main()