
#https://leetcode.com/problems/coin-change-ii/

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def coinchange2(self, A, B):

        noOfWaysToMakeChange = [0]*(B+1)

        noOfWaysToMakeChange[0] = 1

        for coin in A:
            for price in range(1,len(noOfWaysToMakeChange)):
                if coin <= price:
                    noOfWaysToMakeChange[price] += noOfWaysToMakeChange[price-coin]
                    noOfWaysToMakeChange[price] %= (10**6+7)
            #print(noOfWaysToMakeChange)
        return noOfWaysToMakeChange[-1]