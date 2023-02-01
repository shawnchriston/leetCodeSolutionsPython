
#https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        maxPriceAtLengths = [0]*(len(A)+1)

        for length in range(1,len(A)+1):
            for idx in range(1,length+1):
                priceAtLength = A[idx-1]
                maxPriceAtLengths[length] = max(maxPriceAtLengths[length], priceAtLength+maxPriceAtLengths[length - idx])
            #print(maxPriceAtLengths)
        return maxPriceAtLengths[-1]