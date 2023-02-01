#https://leetcode.com/problems/palindrome-partitioning/
class Solution:
    # @param A : string
    # @return an integer
    def minCut(self, A):
        dp = [[False ] *len(A) for _ in range(len(A))]  # store if the substring [i,j] is a palindrome

        for i in range(0 ,len(A)):
            for j in range(0 ,len(A)):
                if j+ i >= len(A):
                    break
                if i == 0:
                    dp[j][j] = True
                elif i == 1 and A[j] == A[j + 1]:
                    dp[j][j + 1] = True
                elif A[j] == A[j + i] and dp[j + 1][j + i - 1]:
                    dp[j][j + i] = True

        minPartitions = [float("inf")] * len(A)

        for i in range(len(A)):
            if dp[0][i]:
                minPartitions[i] = 0
            else:
                for j in range(i):
                    if dp[j + 1][i]:
                        minPartitions[i] = min(minPartitions[i], minPartitions[j] + 1)
        return minPartitions[-1]

