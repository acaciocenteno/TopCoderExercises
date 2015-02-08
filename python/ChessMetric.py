#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://community.topcoder.com/stat?c=problem_statement&pm=1592&rd=4482

from unittest import TestCase, main

class ChessMetric:
    def howMany(self, size, start, end, numMoves):
        # Size-dimensional array, where each dimension represents an iteration.
        # On each dimension we have a Size x Size board (list of rows) and each
        # element of this board (space) is a set of nodes that reached that space
        # at that iteration.
        cnt   = [[[0 for i in xrange(size)] for j in xrange(size)] for k in xrange(numMoves)]
        cur_pos = set([start])
        moves = [          (-1, -2),          (1, -2),
                 (-2, -1), (-1, -1), (0, -1), (1, -1), (2, -1),
                           (-1,  0),          (1,  0),
                 (-2, 1),  (-1, 1),  (0,  1), (1,  1), (2,  1),
                           (-1, 2),           (1, 2)           ]

        for i in xrange(numMoves):
            end_pos = set()
            for pos in cur_pos:
                # Find where could we go from here, and update the
                # destination cell's counter
                for move in moves:
                    dst = (pos[0] + move[0], pos[1] + move[1])
                    if dst[0] < 0 or dst[0] > size - 1:
                        # invalid pos
                        continue
                    if dst[1] < 0 or dst[1] > size - 1:
                        # invalid pos
                        continue
                    # So we have a valid destination, mark on the destination
                    # that we reached it coming from pos, at iteration i.
                    if i > 0:
                        cnt[i][dst[0]][dst[1]] += cnt[i-1][pos[0]][pos[1]]
                    else:
                        cnt[i][dst[0]][dst[1]] += 1
                    end_pos.add(dst)

            cur_pos = end_pos

        return cnt[numMoves-1][end[0]][end[1]]


    def __call__(self, size, start, end, numMoves):
        return self.howMany(size, start, end, numMoves)


class TestChessMetric(TestCase):
    def setUp(self):
        self.inst = ChessMetric()

    def test_00(self):
        size = 3
        start = (0, 0)
        end = (1, 0)
        moves = 1
        exp = 1
        ret = self.inst(size, start, end, moves)
        self.assertEqual(ret, exp)


    def test_01(self):
        size = 3
        start = (0, 0)
        end = (1, 2)
        moves = 1
        exp = 1
        ret = self.inst(size, start, end, moves)
        self.assertEqual(ret, exp)


    def test_02(self):
        size = 3
        start = (0, 0)
        end = (2, 2)
        moves = 1
        exp = 0
        ret = self.inst(size, start, end, moves)
        self.assertEqual(ret, exp)


    def test_03(self):
        size = 3
        start = (0, 0)
        end = (0, 0)
        moves = 2
        exp = 5
        ret = self.inst(size, start, end, moves)
        self.assertEqual(ret, exp)


    def test_04(self):
        size = 100
        start = (0, 0)
        end = (0, 99)
        moves = 50
        exp = 243097320072600
        ret = self.inst(size, start, end, moves)
        self.assertEqual(ret, exp)


if __name__ == '__main__':
    main()