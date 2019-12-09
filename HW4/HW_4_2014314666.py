def DFSUtil(graph, v, visited): 
  
    visited[v] = True			 	# Mark the current node as visited and print it 
    print(v, end = ' ') 
  
    for i in graph[v]: 			 	# Recur for all the vertices adjacent to this vertex
        if visited[i] == False: 
            DFSUtil(graph, i, visited) 


def DFS(graph, v):
    List = []
    for i in range(len(graph)):
        tmp = []
        for j in range(len(graph[i])):
            if graph[i][j] == 1:
                tmp.append(j)
        List.append(tmp)

    graph = List
    visited = [False] * (len(graph))	 # Mark all the vertices as not visited
    DFSUtil(graph, v, visited)
    
    print()

def BFS(graph, s): 
    List = []
    for i in range(len(graph)):
        tmp = []
        for j in range(len(graph[i])):
            if graph[i][j] == 1:
                tmp.append(j)
        List.append(tmp)

    graph = List
    visited = [False] * (len(graph)) 		 # Mark all the vertices as not visited
  
    queue = [] 					 # Create a queue for BFS
  
    queue.append(s) 			 # Mark the source node as visited and enqueue it
    visited[s] = True
  
    while queue: 
  
        s = queue.pop(0) 			 # Dequeue a vertex from queue and print it
        print (s, end = " ") 

        for i in graph[s]: 			# Get all adjacent vertices of the dequeued vertex s. 
            if visited[i] == False: 		# If a adjacent has not been visited, 
                    queue.append(i) 		# then mark it visited and enqueue it 
                    visited[i] = True


if __name__ == "__main__":
    graph = [\
        [0,1,1,0,0,0,0,1],\
        [1,0,0,1,0,1,0,1],\
        [1,0,0,0,0,1,1,0],\
        [0,1,0,0,1,0,0,1],\
        [0,0,0,1,0,0,0,1],\
        [0,1,1,0,0,0,0,0],\
        [0,0,1,0,0,0,0,0],\
        [1,1,0,1,1,0,0,0]]
    DFS(graph,0)
    BFS(graph,0)