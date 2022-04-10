class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(1001)]
        rank = [1]*1001
        
        def find(u):
            p = par[u]
            while par[p]!=p:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(u,v):
            u1,v1 = find(u),find(v)
            
            if u1==v1:
                return True
            else:
                if rank[u1]>rank[v1]:
                    rank[u1]+=v1
                    par[v1]=u1
                else:
                    rank[v1]+=rank[u1]
                    par[u1]=v1
                return False
        
        for u,v in edges:
            if union(u,v):
                return [u,v]