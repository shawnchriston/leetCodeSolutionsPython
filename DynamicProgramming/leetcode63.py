#https://leetcode.com/problems/unique-paths-ii/
class Solution:
	# @param A : list of list of integers
	# @return an integer
	def uniquePathsWithObstacles(self, A):
        return self.uniquePathHelper(len(A)-1, len(A[0])-1, A)

    def uniquePathHelper(self, row, col, A):
        if row < 0 or col < 0:
            return 0
        #base case
        if row == 0 and col == 0:
            if A[0][0] == 0:
                return 1
            else:
                return 0

        if A[row][col] == 1:
            return 0
        else:
            x = self.uniquePathHelper(row-1,col,A)
            y = self.uniquePathHelper(row, col-1, A)

            return x+y


