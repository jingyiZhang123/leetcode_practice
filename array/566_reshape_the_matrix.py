"""
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input:
nums =
[[1,2],
 [3,4]]
r = 1, c = 4
Output:
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
Example 2:
Input:
nums =
[[1,2],
 [3,4]]
r = 2, c = 4
Output:
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.
"""

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        origin_width, origin_height = len(nums[0]), len(nums)
        new_width, new_height = c, r
        if origin_width * origin_height != new_width * new_height:
            return nums
        new_matrix = [[0 for j in range(new_width)] for i in range(new_height)]

        origin_i = origin_j = 0
        for i in range(new_height):
            for j in range(new_width):
                new_matrix[i][j] = nums[origin_i][origin_j]
                origin_j = origin_j+1
                if origin_j >= origin_width:
                    origin_j = 0
                    origin_i += 1

        return new_matrix


print(Solution().matrixReshape([[1,2],[3,4]], 4, 1))









