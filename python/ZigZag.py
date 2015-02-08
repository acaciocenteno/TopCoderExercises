#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase, main


class ZigZag:
	class Element:
		def __init__(self):
			self.sz = 1
			self.prev = None
			self.signal = 0

	def longestZigZag(self, sequence):
		sz   = len(sequence)
		itms = [ ZigZag.Element() for i in xrange(sz) ]

		for i in xrange(1, sz):
			for j in xrange(i-1, -1, -1):
				df = sequence[i] - sequence[j]
				if df == 0:
					continue
				elif df < 0:
					df = -1
				else:
					df = 1
				if itms[j].signal != df and itms[j].sz + 1 > itms[i].sz:
					itms[i].sz = itms[j].sz + 1
					itms[i].signal = df
					itms[i].prev = j

		return itms[sz-1].sz

	def __call__(self, sequence):
		return self.longestZigZag(sequence)


class TestZigZag(TestCase):
	def setUp(self):
		self.inst = ZigZag()

	def test_00(self):
		seq = [ 1, 7, 4, 9, 2, 5 ]
		exp = 6
		ret = self.inst(seq)

		self.assertEqual( ret, exp )

	def test_01(self):
		seq = [ 1, 17, 5, 10, 13, 15, 10, 5, 16, 8 ]
		exp = 7
		ret = self.inst(seq)

		self.assertEqual( ret, exp )

	def test_02(self):
		seq = [ 44 ]
		exp = 1
		ret = self.inst(seq)

		self.assertEqual( ret, exp )

	def test_03(self):
		seq = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
		exp = 2
		ret = self.inst(seq)

		self.assertEqual( ret, exp )

	def test_04(self):
		seq = [ 70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32 ]
		exp = 8
		ret = self.inst(seq)

		self.assertEqual( ret, exp )

	def test_05(self):
		seq = [ 374, 40, 854, 203, 203, 156, 362, 279, 812, 955, 
				600, 947, 978, 46, 100, 953, 670, 862, 568, 188, 
				67, 669, 810, 704, 52, 861, 49, 640, 370, 908, 
				477, 245, 413, 109, 659, 401, 483, 308, 609, 120, 
				249, 22, 176, 279, 23, 22, 617, 462, 459, 244 ]
		exp = 36
		ret = self.inst(seq)

		self.assertEqual( ret, exp )

if __name__ == '__main__':
	main()