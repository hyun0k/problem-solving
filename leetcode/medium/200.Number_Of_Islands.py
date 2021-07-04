class Solution(object):
    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        """[summary]
        dfs 재귀를 이용한 풀이. python에서 재귀호출 횟수를 1000으로 제한을 두기 때문에 RecursionError발생.
        """
        def dfs(i: 'int', j: 'int'):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0] or grid[i][j] != '1'):
                return
            
            grid[i][j] = '0'

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count



# solution = Solution()
# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# print(solution.numIslands(grid))

        