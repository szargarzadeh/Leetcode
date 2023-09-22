class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        num_col = 0
        length = 0

        while length < len(s):
            if num_col % (numRows - 1) == 0:
                num_col += 1
                length += numRows
            else:
                num_col += (numRows - 2)
                length += (numRows - 2)

        matrix = [["" for i in range(num_col)] for j in range(numRows)]
        idx = 0
        col, row = 0, 0
        while idx < len(s):
            if col % (numRows - 1) == 0:
                for i in range(numRows):
                    if idx >= len(s):
                        break
                    matrix[i][col] = s[idx]
                    idx += 1
                col += 1
            else:
                for i in range(numRows - 2, 0, -1):
                    if idx >= len(s):
                        break
                    matrix[i][col] = s[idx]
                    col += 1
                    idx += 1

        res = ""
        for row in range(numRows):
            for col in range(num_col):
                if matrix[row][col]:
                    res += matrix[row][col]

        return res


