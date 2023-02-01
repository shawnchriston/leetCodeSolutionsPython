

#https://leetcode.com/problems/distinct-subsequences/
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def numDistinct(self, A, B):
        dp = [[0 ] *(len(A ) +1) for _ in range(len(B ) +1) ]

        # base case
        for j in range(len(dp[1])):
            dp[0][j] = 1

        # print(dp)

        for i in range(1 ,len(dp)):
            for j in range(1 ,len(dp[0])):
                if B[ i -1] == A[ j -1]:
                    dp[i][j] = dp[ i -1][ j -1] + dp[i][ j -1]
                else:
                    dp[i][j] = dp[i][ j -1]
        # print(dp)

        return dp[-1][-1]



