class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        dp = [[0] * len(A) for _ in range(len(A))]  # store if the substring [i,j] is a palindrome

        for i in range(0, len(A)):
            for j in range(0, len(A)):
                if j + i >= len(A):
                    break
                if i == 0:
                    dp[j][j] = 1
                elif i == 1:
                    if A[j] == A[j + 1]:
                        dp[j][j + 1] = 2
                    else:
                        dp[j][j + 1] = 1
                else:
                    if A[j] == A[j + i]:
                        dp[j][j + i] = 2 + dp[j + 1][j + i - 1]
                    else:
                        dp[j][j + i] = max(dp[j + 1][j + i], dp[j][j + i - 1])
        # print(dp)
        return dp[0][-1]


