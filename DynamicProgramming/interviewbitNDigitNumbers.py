#https://www.interviewbit.com/problems/n-digit-numbers-with-digit-sum-s-/

class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
    count = 0
	def solve(self, A, B):
        self.solveHelper(0, A, B, [0]*(B+1))
        return self.count

    def solveHelper(self,currVal, A, B, storage):
        if len(str(currVal)) == A:
            if self.sumHelper(currVal) == B:
                self.count +=1
            return
        for ele in range(0,10):
            if currVal*10+ele > 0 and currVal*10+ele <= B:
                if storage[currVal*10+ele] == 0:
                    storage[currVal*10+ele] = self.solveHelper(currVal*10+ele, A, B, storage)
                return storage[currVal*10+ele]

    def sumHelper(self, num):
        temp = 0
        while num>0:
            temp+= num%10
            num = num//10
        return temp


