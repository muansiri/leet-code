class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        for i in range(rowIndex + 1):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ans[i - 1][j - 1] + ans[i - 1][j])
            ans.append(row)
        return ans[rowIndex]
