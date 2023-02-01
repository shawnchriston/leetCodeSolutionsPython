#https://leetcode.com/problems/triangle/


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        storage = []

        storage.append(A[0])  # base case

        for idx in range(1, len(A)):
            storage.append([0] * len(A[idx]))

            for eleIdx in range(len(A[idx])):
                if eleIdx == 0:
                    storage[idx][0] = A[idx][0] + storage[idx - 1][0]
                elif eleIdx == len(A[idx]) - 1:
                    storage[idx][eleIdx] = A[idx][eleIdx] + storage[idx - 1][-1]
                else:
                    storage[idx][eleIdx] = A[idx][eleIdx] + min(storage[idx - 1][eleIdx - 1], storage[idx - 1][eleIdx])

        return min(storage[-1])
