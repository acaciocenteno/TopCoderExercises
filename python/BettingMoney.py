#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase, main

class BettingMoney:
	def moneyMade(self, amounts, centsPerDollar, finalResult):
		total = sum(amounts) * 100
		payment = amounts[finalResult] * 100 + (amounts[finalResult] * centsPerDollar[finalResult])
		return total - payment


class TestBettingMoney(TestCase):
	def setUp(self):
		self.bm = BettingMoney()

	def test_00(self):
		amounts   = [ 10, 20, 30 ]
		centspd   = [ 20, 30, 40 ]
		finalRslt = 1
		exp       = 3400
		ret       = self.bm.moneyMade(amounts, centspd, finalRslt)

		self.assertEqual( exp, ret )


	def test_01(self):
		amounts   = [ 200, 300, 100 ]
		centspd   = [ 10, 10, 10 ]
		finalRslt = 2
		exp       = 49000
		ret       = self.bm.moneyMade(amounts, centspd, finalRslt)

		self.assertEqual( exp, ret )


	def test_02(self):
		amounts   = [ 100, 100, 100, 100 ]
		centspd   = [ 5, 5, 5, 5 ]
		finalRslt = 0
		exp       = 29500
		ret       = self.bm.moneyMade(amounts, centspd, finalRslt)

		self.assertEqual( exp, ret )


	def test_03(self):
		amounts   = [ 5000, 5000 ]
		centspd   = [ 100, 2 ]
		finalRslt = 0
		exp       = 0
		ret       = self.bm.moneyMade(amounts, centspd, finalRslt)

		self.assertEqual( exp, ret )


	def test_04(self):
		amounts   = [ 100 ]
		centspd   = [ 10 ]
		finalRslt = 0
		exp       = -1000
		ret       = self.bm.moneyMade(amounts, centspd, finalRslt)

		self.assertEqual( exp, ret )


if __name__ == '__main__':
	main()