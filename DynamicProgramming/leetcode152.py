#https://leetcode.com/problems/maximum-product-subarray/
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        maxx = [1] * len(A)
        minn = [1] * len(A)

        maxx[0] = A[0]
        minn[0] = A[0]

        result = A[0]

        for idx in range(1, len(A)):
            ele = A[idx]
            maxx[idx] = max(ele, maxx[idx - 1] * ele, minn[idx - 1] * ele)
            minn[idx] = min(ele, maxx[idx - 1] * ele, minn[idx - 1] * ele)

            result = max(result, maxx[idx], minn[idx])
        return result

