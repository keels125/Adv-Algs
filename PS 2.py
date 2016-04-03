#Keely Hicks
#COMP 330--Problem Set 2

from queue import Queue

def parseInput(string):
    adjMatrix = []
    string = string[1:-1]
    string = string.replace(' ', '')
    lines = string.split('],')
    for line in lines:
        line = line.replace('[', '').replace(']', '')
        nums = line.split(',')
        adjMatrix.append([])
        for num in nums:
            adjMatrix[-1].append(int(num))
    return adjMatrix

def makeAdjList(matrix): #given an adj matrix, convert to an adj list
    adjList = {} #empty dictionary
    for row in range(0, len(matrix)): #iterate over rows
        for col in range(0, len(matrix)): #iterate over columns
            key=row+1 #+1 accounts for 0 indexing
            adjList.setdefault(key, []) #this allows us to append multiple adj vertices
            if matrix[row][col]==1:
                adjList[key].append(col+1) #update the current vertex with next adj vertex
                
    return adjList
          
def BFS(start, adjList):
    visited=[] #store the visited vertices
    visited.append(start)
    q=Queue() #initialize queue
    q.put(start) #contain only the start vertex at first
    while (not q.empty()): #while we still have vertices to visit
        vert=q.get() #get the next vertice
        for adj in adjList.get(vert): #for all adjacent vertices
            if not (adj in visited): 
                visited.append(adj) #if not already visited, mark visited
                q.put(adj) #put it in the queue
    return visited


def DFS(start, adjList, visited):
    visited.append(start) #mark start as visited
    for adj in adjList.get(start): #for each adjacent vertex
        if not (adj in visited): #if not already visited
            DFS(adj, adjList, visited) #recursively call DFS on vertex
    return visited

def main():
    strInput = input("Please enter your graph's adjacency matrix: ")
    adjMatrix = parseInput(strInput) #create matrix with input
    adjList = makeAdjList(adjMatrix) #convert matrix to list
    print("\nBFS:\n")
    for i in range (0, len(adjList)):
        print(BFS(i+1, adjList)) #print BFS traversal for each starting vertex
    print("\nDFS:\n")
    for i in range (0, len(adjList)):
        print(DFS(i+1, adjList, [])) #print DFS traversal for each starting vertex
    

main()
