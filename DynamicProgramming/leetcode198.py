#https://leetcode.com/problems/house-robber/
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        odd = 0
        even = 0

        result = [0 ] *len(A[0])

        result[0] = max(A[0][0], A[1][0])


        for i in range(1 ,len(A[0])):
            if i > 1:
                result[i] = max( max(A[1][i], A[0][i]) +result[i - 2], result[i - 1])

            else:
                result[i] = max(max(A[1][i], A[0][i]), result[i - 1])

        return result[-1]