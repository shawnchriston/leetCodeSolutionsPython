#https://www.interviewbit.com/problems/tushars-birthday-party/
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def solve(self, A, B, C):
        minCosts = [float("inf")] * (max(A) + 1)

        minCosts[0] = 0
        # print(minCosts)
        for capacity in range(1, len(minCosts)):
            for idx in range(len(B)):
                capacityOfDish = B[idx]
                cost = C[idx]
                if capacityOfDish <= capacity:
                    minCosts[capacity] = min(minCosts[capacity], cost + minCosts[capacity - capacityOfDish])
        ans = 0
        for friend in A:
            ans += minCosts[friend]

        return ans

