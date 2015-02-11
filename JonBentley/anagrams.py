#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# Anagrams: Implements Jon Bentley's description of the solution to the problem:
# Given a dictionary, find all anagrams.

# On a modern computer, even doing so many copies and doing all the sorting in memory,
# with a 235k words dict, it took less than 2 seconds to find:
# $ time ./anagrams.py /usr/share/dict/words > anagrams.txt
#
# real	0m1.613s
# user	0m1.555s
# sys	0m0.055s
#
# Neat! Maybe worth reimplementing in C++ tomorrow to compare.

# Phase 1: Signature (Nowadays this would be called 'Map')
def sign(filename):
	signed = []

	with open(filename, 'r') as f:
		for line in f:
			sanitized = line[:-1]
			signature = sorted( list(sanitized) )
			signed.append( (signature, sanitized) )

	return signed


# Phase 2: Group by signature (Nowadays this would be called 'Combine')
def sort(signed):
	return sorted(signed)


# Phase 3: Print anagrams (Nowadays this would be called 'Reduce')
def squash(srtd):
	cur_key = srtd[0][0]
	cur_idx = 0

	for i in xrange(len(srtd)):
		if srtd[i][0] != cur_key:
			if i - cur_idx > 1:
				print ' '.join( [ srtd[x][1] for x in xrange(cur_idx, i) ] )
			cur_idx = i
			cur_key = srtd[i][0]

	if len(srtd) - i > 1:
		print ' '.join( [ srtd[x][1] for x in xrange(cur_idx, len(srtd)) ] )


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print 'Please, specify a dictionary file.'
		sys.exit(1)

	try:
		signed = sign(sys.argv[1])
	except OSError:
		print 'File [{0}] does not exist or is not accessible.'
		sys.exit(2)

	srtd = sort(signed)
	squash(srtd)
