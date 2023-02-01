#https://leetcode.com/problems/longest-increasing-subsequence/
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        LisLength = [0 ] *len(A)
        ListPrev = [-1 ] *len(A)
        maxIndex = -1
        maxLen = 0
        for i in range(len(A)):
            tempLen = 0
            for j in range(i):
                if A[j] < A[i] and LisLength[j] > LisLength[i ] -1:
                    LisLength[i] = LisLength[j ] +1
                    ListPrev[i] = j
                    if LisLength[i] > maxLen:
                        maxIndex = i
                        maxLen = LisLength[i]

        # print(maxLen, maxIndex)
        stack = []
        while maxLen >= 0:
            # print(maxIndex, maxLen)
            stack.append(A[maxIndex])
            maxIndex = ListPrev[maxIndex]
            maxLen-=1

        return len(stack)


