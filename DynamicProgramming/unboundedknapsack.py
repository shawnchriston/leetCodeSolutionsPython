class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        storage = [0]*(A+1)

        for capacity in range(1,len(storage)):
            for item in range(len(C)):
                weight = C[item]
                value = B[item]

                if weight <= capacity:
                    storage[capacity] = max(storage[capacity], value + storage[capacity - weight])
        return storage[-1]