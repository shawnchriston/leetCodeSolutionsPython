#https://leetcode.com/problems/russian-doll-envelopes/
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):

        A.sort()

        LisLength = [0 ] *len(A)
        ListPrev = [-1 ] *len(A)
        maxIndex = -1
        maxLen = 0
        for i in range(len(A)):
            for j in range(i):
                if A[j][0] < A[i][0] and A[j][1 ] <A[i][1] and LisLength[j] > LisLength[i ] -1:
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