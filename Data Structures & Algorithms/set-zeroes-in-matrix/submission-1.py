class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroes = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroes.append((i, j))

        while zeroes:
            r, c = zeroes.pop()

            for j in range(len(matrix[0])): # change to zeroes in row
                matrix[r][j] = 0
        
            for i in range(len(matrix)): # change to zeroes in col
                matrix[i][c] = 0

        
