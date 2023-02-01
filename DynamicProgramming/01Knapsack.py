class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        storage = [[0]*(C+1) for _ in range(len(A)+1)]

        for item in range(1,len(storage)):
            for capacity in range(1,len(storage[0])):
                weight = B[item-1]
                value = A[item-1]
                if weight <= capacity:
                    storage[item][capacity] = max(storage[item-1][capacity], value + storage[item-1][capacity-weight])
                else:
                    storage[item][capacity] = storage[item-1][capacity]
        return storage[-1][-1]