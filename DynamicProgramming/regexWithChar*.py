class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def isMatch(self, A, B):
        dp = [ [False]*(len(A)+1) for _ in range(len(B)+1) ]

        dp[0][0] = True

        for i in range(2,len(dp),2):
            if B[i-1] == "*":
                dp[i][0] = True
            else:
                break

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if B[i-1] == "*":
                    if B[i-2] == "." or B[i-2] == A[j-1]:
                        dp[i][j] = dp[i-2][j] or dp[i][j-1]
                    else:
                        dp[i][j] = dp[i-2][j]
                elif B[i-1] == "." or B[i-1] == A[j-1]:
                    dp[i][j] = dp[i-1][j-1]


        #print(dp)
        return 1 if dp[-1][-1] else 0