


# Given a string A, find if there is any subsequence that repeats itself.
#
# A subsequence of a string is defined as a sequence of characters generated by deleting some characters in the string without changing the order of the remaining characters.
#
# NOTE:
# 1. Subsequence length should be greater than or equal to 2.
# 2. The repeating subsequence should be disjoint that is in both the sequence no character in the same order and position should be taken from the same index of the original string.


class Solution:
    # @param A : string
    # @return an integer
    def anytwo(self, A):
        dp = [[0 ] *(len(A ) +1) for _ in range(len(A ) +1) ]


        for i in range(1 ,len(dp)):
            for j in range(1 ,len(dp[0])):
                if i!= j and A[i - 1] == A[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    # print(dp)

        return 1 if dp[-1][-1] > 1 else 0
