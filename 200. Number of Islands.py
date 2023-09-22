from collections import defaultdict


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        graph = defaultdict(lambda: [])
        m = len(grid)
        n = len(grid[0])
        ones = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ones += 1
                    if i > 0 and grid[i - 1][j] == "1":
                        graph[(i, j)].append((i - 1, j))

                    if i < m - 1 and grid[i + 1][j] == "1":
                        graph[(i, j)].append((i + 1, j))

                    if j > 0 and grid[i][j - 1] == "1":
                        graph[(i, j)].append((i, j - 1))

                    if j < n - 1 and grid[i][j + 1] == "1":
                        graph[(i, j)].append((i, j + 1))

        visited = defaultdict(lambda: False)

        def dfs(root):
            if visited[root]:
                return
            visited[root] = True
            for neighbor in graph[root]:
                dfs(neighbor)

        count = 0
        for vertex in graph:
            if not visited[vertex]:
                dfs(vertex)
                count += 1

        return count + ones - len(graph.keys())