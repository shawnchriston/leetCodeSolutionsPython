
#https://leetcode.com/problems/shortest-path-in-binary-matrix/

import sys
sys.setrecursionlimit(1 0* *6)
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        storage = [[False ] *len(A[0]) for _ in range(len(A))]
    storage[0][0] = A[0][0]
    self.minPathSumHelper(len(A ) -1, len(A[0] ) -1, A, storage)
    # print(storage)
    return storage[-1][-1]

def minPathSumHelper(self, row, col, A, storage):
    if row == 0 and col = =0:
        return storage[0][0]

    if row < 0 or col < 0:
        return float("inf")

    if storage[row][col] == False:
        left = self.minPathSumHelper(row, co l -1, A, storage)
        up = self.minPathSumHelper(ro w -1, col, A, storage)

        storage[row][col] = A[row][col] + min(left, up)

    return storage[row][col]




