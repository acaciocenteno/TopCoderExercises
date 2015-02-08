#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bisect import bisect_left
from unittest import TestCase, main

def binary_search(l, item, beg=0, end=None):
	end = end if end is not None else len(l)
	pos = bisect_left(l, item, beg, end)
	return pos if (pos != end and l[pos] == item) else -1


class UserName:
	def newMember(self, existingNames, newName):
		names = sorted(existingNames)
		pos = binary_search(names, newName)

		if pos == -1:
			return newName

		for i in xrange(1, len(names)):
			nname = '{0}{1}'.format(newName, i)
			pos = binary_search(names, nname)

			if pos == -1:
				return nname

		# Should never happen
		return None



class TestUserName(TestCase):
	def setUp(self):
		self.u = UserName()

	def test_01(self):
		names = [ "MasterOfDisaster", "DingBat", "Orpheus", "WolfMan", "MrKnowItAll" ]
		name  = "TygerTyger"
		exp   = "TygerTyger"
		ret   = self.u.newMember(names, name)

		self.assertEqual( exp, ret )


	def test_02(self):
		names = [ "MasterOfDisaster", "TygerTyger1", "DingBat", "Orpheus", "TygerTyger", "WolfMan", "MrKnowItAll" ]
		name  = "TygerTyger"
		exp   = "TygerTyger2"
		ret   = self.u.newMember(names, name)

		self.assertEqual( exp, ret )


	def test_03(self):
		names = [ "TygerTyger2000", "TygerTyger1", "MasterDisaster", "DingBat", "Orpheus", "WolfMan", "MrKnowItAll" ]
		name  = "TygerTyger"
		exp   = "TygerTyger"
		ret   = self.u.newMember(names, name)

		self.assertEqual( exp, ret )


	def test_04(self):
		names = [ "grokster2", "BrownEyedBoy", "Yoop", "BlueEyedGirl", "grokster", "Elemental", "NightShade", "Grokster1" ]
		name  = "grokster"
		exp   = "grokster1"
		ret   = self.u.newMember(names, name)

		self.assertEqual( exp, ret )


	def test_05(self):
		names = [ 	"Bart4", "Bart5", "Bart6", "Bart7", "Bart8", "Bart9", "Bart10",
 					"Lisa", "Marge", "Homer", "Bart", "Bart1", "Bart2", "Bart3",
 					"Bart11", "Bart12" 	]
		name  = "Bart"
		exp   = "Bart13"
		ret   = self.u.newMember(names, name)

		self.assertEqual( exp, ret )


if __name__ == '__main__':
	main()