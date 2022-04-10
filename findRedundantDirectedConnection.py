class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        #print(edges)
        
        n = len(edges)
        graph = {i+1:set() for i in range(n)}
        indegree = {i+1:0 for i in range(n)}
        
        for a,b in edges:
            graph[a].add(b)
            indegree[b]+=1

        
        for i in range(n-1,-1,-1):
            a,b = edges[i]
            graph[a].remove(b)
            indegree[b]-=1
            if self.found_all(graph,indegree,n):
                return [a,b]
            graph[a].add(b)
            indegree[b]+=1
           

            
        return [-1,-1]
            
    
    def found_all(self,graph,indegree,n):
        #print(graph,indegree,n)
        
        visited = set()
        que = deque()
        
        for i in range(1,n+1):
            if indegree[i] == 0:
                que.append(i)
                
        if len(que) != 1:
            return False
        
        found = 0
        
        while que:
            el = que.popleft()
            found +=1
            visited.add(el)
            for x in graph[el]:
                if x not in visited:
                    que.append(x)
                else:
                    return False
        return found == n