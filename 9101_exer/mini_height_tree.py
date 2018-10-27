from collections import deque
class Solution:
    """
    @param n: n nodes labeled from 0 to n - 1
    @param edges: a undirected graph
    @return:  a list of all the MHTs root labels
    """
    def findMinHeightTrees(self, n, edges):
        graph = [set() for _ in range(n)]
        for v,w in edges:
            graph[v].add(w)
            graph[w].add(v)
        
        wlist = deque()
        for i in range(n):
            if len(graph[i]) == 1:
                wlist.append(i)
        
        steps = 0
        node1, node2 = n,n
        while(wlist):
            steps += 1
            len_level = len(wlist)
            
            if len_level == 1:
                return list(wlist)
            for i in range(len_level):
                prev_node1 = node1
                node1 = wlist.popleft()
                if node1 == node2:
                    return [node1,prev_node1]
                node2 = graph[node1].pop() 
                graph[node2].remove(node1)
                if (len(graph[node2]) == 1):
                    wlist.append(node2)
        return  list(wlist) 



print(Solution().findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))