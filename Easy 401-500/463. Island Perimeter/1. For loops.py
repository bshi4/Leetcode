class Solution:
    def islandPerimeter(self, grid):
        land = 0
        c = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    land += 1
                    if i > 0 and grid[i-1][j] == 1:
                        c += 1
                    if j > 0 and grid[i][j-1] == 1:
                        c += 1
        return land*4-c*2