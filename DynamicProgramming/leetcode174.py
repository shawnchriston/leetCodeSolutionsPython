#https://leetcode.com/problems/dungeon-game/

import sys
sys.setrecursionlimit(10**6)
class Solution:
	# @param A : list of list of integers
	# @return an integer
	def calculateMinimumHP(self, A):
        storage = [ [False]*len(A[0]) for _ in range(len(A)) ]
        storage[-1][-1] = max(1, 1-A[-1][-1])
        self.calculateMinimumHPHelper(0,0, A, storage)

        return storage[0][0]



    def calculateMinimumHPHelper(self, row, col, A, storage):
        if row >= len(A) or col >= len(A[0]):
            return float("inf")

        if storage[row][col] == False:

            top = self.calculateMinimumHPHelper(row+1, col, A, storage)
            left = self.calculateMinimumHPHelper(row, col+1, A, storage)
            storage[row][col] = max(1,min(top, left)-A[row][col])

        return storage[row][col]