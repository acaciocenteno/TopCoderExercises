#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase, main


class Coins:
	def find(self, amounts, objective):
		mins  = [ 9999999 for i in xrange(objective + 1) ]
		path  = [ 0 for i in xrange(objective + 1) ]
		coins = []

		mins[0] = 0
		N = len(amounts)

		for i in xrange(1, objective + 1):
			for cur in amounts:
				if cur > i:
					break
				if mins[i - cur] + 1 < mins[i]:
					path[i] = cur
					mins[i] = mins[i - cur] + 1
		
		i = objective
		while i > 0:
			coin = path[i]
			coins.append(coin)
			i -= coin

		#print mins
		#print path
		#print coins

		return (mins[objective], coins)



class TestCoins(TestCase):
	def setUp(self):
		self.c = Coins()

	def test_00(self):
		amounts = [ 1, 3, 5 ]
		obj     = 11
		exp     = (3, [1, 5, 5])
		ret     = self.c.find(amounts, obj)

		self.assertEqual( exp, ret )


	def test_01(self):
		amounts = [ 1, 3, 5 ]
		obj     = 13
		exp     = (3, [3, 5, 5])
		ret     = self.c.find(amounts, obj)

		self.assertEqual( exp, ret )


	def test_02(self):
		amounts = [ 1, 3, 5 ]
		obj     = 17
		exp     = (5, [1, 1, 5, 5, 5])
		ret     = self.c.find(amounts, obj)

		self.assertEqual( exp, ret )


	def test_03(self):
		amounts = [ 1, 3, 5 ]
		obj     = 18
		exp     = (4, [3, 5, 5, 5])
		ret     = self.c.find(amounts, obj)

		self.assertEqual( exp, ret )


if __name__ == '__main__':
	main()