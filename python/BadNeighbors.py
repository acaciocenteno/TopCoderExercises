#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://community.topcoder.com/stat?c=problem_statement&pm=2402&rd=5009

from unittest import TestCase, main

class BadNeighbors:
	class Element:
		def __init__(self, val):
			self.val = val
			self.prev = None
			# Hack to avoid having to "rewind" at last iteration
			self.inc_zero = False

	def maxDonations(self, sequence):
		sz   = len(sequence)
		itms = [ BadNeighbors.Element( val ) for val in sequence ]
		mval = max(sequence[:2])
		itms[0].inc_zero = True

		for i in xrange(2, sz):
			for j in xrange(i-2, -1, -1):
				val = sequence[i] + itms[j].val

				if i == sz - 1 and itms[j].inc_zero:
					# This is the rewind the inc_zero flag avoids:
					# prev = itms[j].prev				
					# while prev is not None:
					# 	if prev == 0:
					# 		val -= sequence[0]
					# 	prev = itms[prev].prev
					val -= sequence[0]

				if val > itms[i].val:
					itms[i].val  = val
					itms[i].prev = j
					itms[i].inc_zero = itms[j].inc_zero
				if val > mval:
					mval = val

		return mval

	def __call__(self, sequence):
		return self.maxDonations(sequence)


class TestBadNeighbors(TestCase):
	def setUp(self):
		self.inst = BadNeighbors()

	def test_00(self):
		seq = [ 10, 3, 2, 5, 7, 8 ]
		exp = 19
		ret = self.inst(seq)

		self.assertEqual( ret, exp )

	def test_01(self):
		seq = [ 11, 15 ]
		exp = 15
		ret = self.inst(seq)

		self.assertEqual( ret, exp )

	def test_02(self):
		seq = [ 7, 7, 7, 7, 7, 7, 7 ]
		exp = 21
		ret = self.inst(seq)

		self.assertEqual( ret, exp )

	def test_03(self):
		seq = [ 1, 2, 3, 4, 5, 1, 2, 3, 4, 5 ]
		exp = 16
		ret = self.inst(seq)

		self.assertEqual( ret, exp )

	def test_04(self):
		seq = [ 94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61,  
  				6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397,
  				52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72 ]
		exp = 2926
		ret = self.inst(seq)

		self.assertEqual( ret, exp )


if __name__ == '__main__':
	main()