from collections import deque

class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)
        target = (1 << n) - 1
        visited = set() 
        
        queue = deque([(i, 1 << i, 0) for i in range(n)])  
        
        while queue:
            node, state, steps = queue.popleft()
            
            if state == target:
                return steps
            
            if (node, state) in visited:
                continue
            
            visited.add((node, state))
            
            for neighbor in graph[node]:
                queue.append((neighbor, state | (1 << neighbor), steps + 1))
        
        return -1 


graph1 = [[1,2,3],[0],[0],[0]]
graph2 = [[1],[0,2,4],[1,3,4],[2],[1,2]]

sol = Solution()
print(sol.shortestPathLength(graph1))  
print(sol.shortestPathLength(graph2))  
