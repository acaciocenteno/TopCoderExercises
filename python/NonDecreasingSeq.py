#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase, main


class Sequence:
	def non_dec(self, seq):
		sz = len(seq)		
		longest = [ 1    for i in xrange(sz) ]
		states  = [ None for i in xrange(sz) ]
		path    = []

		for i in xrange(1, sz):
			cur = i
			for j in xrange(i-1, -1, -1):
				if seq[j] <= seq[i] and longest[j] + 1 > longest[i]:
					longest[i] = longest[j] + 1
					states[i]  = j
					

		while cur is not None:
			path.append( seq[cur] )
			cur = states[cur]

		path = sorted(path)

		return (longest[sz-1], path)



class TestSequence(TestCase):
	def setUp(self):
		self.s = Sequence()

	def test_00(self):
		seq = [ 5, 3, 4, 8, 6, 7 ]
		exp = (4, [3, 4, 6, 7])
		ret = self.s.non_dec(seq)

		self.assertEqual( ret, exp )


	def test_01(self):
		seq = [ 13, 14, 6, 2, 5, 3, 4, 8, 12, 17 ]
		exp = (6, [ 2, 3, 4, 8, 12, 17 ])
		ret = self.s.non_dec(seq)

		self.assertEqual( ret, exp )


	def test_02(self):
		seq = [ i for i in xrange(10, 0, -1) ]
		exp = (1, [ 1 ])
		ret = self.s.non_dec(seq)

		self.assertEqual( ret, exp )


	def test_03(self):
		seq = [ i for i in xrange(10) ]
		exp = (10, [ i for i in xrange(10) ])
		ret = self.s.non_dec(seq)

		self.assertEqual( ret, exp )


	def test_04(self):
		seq = [ 10 for i in xrange(10) ]
		exp = (10, [ 10 for i in xrange(10) ])
		ret = self.s.non_dec(seq)

		self.assertEqual( ret, exp )


if __name__ == '__main__':
	main()