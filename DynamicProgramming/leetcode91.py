#https://leetcode.com/problems/decode-ways/

class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        n = len(A)
        MOD = 1000000007

        # Bottom-up DP
        dp = [0] * (n + 1)
        dp[n] = 1

        for idx in reversed(range(0, n)):
            string_val = A[idx]

            if string_val != '0':
                dp[idx] += dp[idx + 1]

            if idx + 1 < n and (A[idx] == '1' or A[idx] == '2' and A[idx + 1] <= '6'):
                dp[idx] += dp[idx + 2]

        return dp[0] % MOD