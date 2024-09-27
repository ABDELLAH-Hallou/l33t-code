
from collections import defaultdict
from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        e = len(connections)
        if e == (n*(n-1))/2 and n>2:
            return []
        neighbors = defaultdict(list)
        for edge in connections:
            neighbors[edge[0]].append(edge[1])
            neighbors[edge[1]].append(edge[0])
        
        connections = set(map(tuple, (map(sorted, connections))))
        rank = [-2] * n
        
        def dfs(node, depth):
            if rank[node] >= 0:
                return rank[node]
            rank[node] = depth
            min_back_depth = n
            for neighbor in neighbors[node]:
                if rank[neighbor] == rank[node] - 1:
                    continue
                back_depth = dfs(neighbor, depth + 1)
                if back_depth <= depth:
                    connections.discard(tuple(sorted((node, neighbor))))
                min_back_depth = min(min_back_depth, back_depth)
            return min_back_depth
            
        dfs(0, 0)
        return list(connections) 