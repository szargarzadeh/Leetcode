from collections import defaultdict
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:


        graph = defaultdict(lambda: [])
        m = len(maze)
        n = len(maze[0])

        for i in range(m):
            for j in range(n):
                #right
                cur_i = i
                while cur_i < m and maze[cur_i][j] == 0:
                    cur_i += 1
                if cur_i - 1 != i:
                    graph[(i, j)].append((cur_i - 1, j))

                #left
                cur_i = i
                while cur_i >= 0 and maze[cur_i][j] == 0:
                    cur_i -= 1
                if cur_i + 1 != i:
                    graph[(i, j)].append((cur_i + 1, j))

                #down
                cur_j = j
                while cur_j < n and maze[i][cur_j] == 0:
                    cur_j += 1
                if cur_j - 1 != j:
                    graph[(i, j)].append((i, cur_j - 1))

                #up
                cur_j = j
                while cur_j >= 0 and maze[i][cur_j] == 0:
                    cur_j -= 1
                if cur_j + 1 != j:
                    graph[(i, j)].append((i, cur_j + 1))

        visited = set()
        def dfs(root):
            if root in visited:
                return
            visited.add(root)
            for neighbor in graph[root]:
                dfs(neighbor)


        dfs((start[0], start[1]))
        return (destination[0], destination[1]) in visited

