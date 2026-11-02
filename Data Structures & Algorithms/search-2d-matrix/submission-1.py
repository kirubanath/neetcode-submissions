class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N,M = len(matrix), len(matrix[0])

        # Flatten the matrix into an array
        l = 0
        r = N*M -1

        while l<=r:

            m = (l+r)//2
            row = m//M
            col = m%M

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = m+1
            else:
                r = m-1
        
        return False

