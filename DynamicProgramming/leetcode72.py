#https://leetcode.com/problems/edit-distance/


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

        for i in range(0, len(dp)):
            for j in range(0, len(dp[0])):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i

                elif A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
        # print(dp)
        return dp[-1][-1]

