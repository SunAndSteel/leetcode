class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        convertedS = [""] * numRows
        index, step = 0, 1

        for char in s:
            convertedS[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(convertedS)


s = Solution()
print(s.convert("PAYPALISHIRING", 3))
print("PAHNAPLSIIGYIR" == s.convert("PAYPALISHIRING", 3))
