def dfs(aGraph, root): 
    stack = [root] 
    parents = {root: root} 
    path = list 
    while stack: 
        print ('Stack is: %s' % stack) 
        vertex = stack.pop(-1) 
        print ('Working on %s' % vertex) 
        for element in aGraph[vertex]: 
            if element not in parents: 
                parents[element] = vertex 
                stack.append(element)
                print ('Now, adding %s to the stack' % element) 
                path.append(parents[vertex]+'>'+vertex) 
    return path[1:]

g = dict() 
g['Amine'] = ['Wassim', 'Nick', 'Mike','Elena'] 
g['Wassim'] = ['Amine', 'Imran'] 
g['Nick'] = ['Amine'] 
g['Mike'] = ['Amine', 'Mary'] 
g['Elena'] = ['Amine'] 
g['Imran'] = ['Wassim', 'Steven'] 
g['Mary'] = ['Mike']
g['Steven'] = ['Imran']

dfs(g,"Amine")