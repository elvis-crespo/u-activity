import time

# start time
startTime = time.perf_counter()

class Graph:
    class Edge:
        def __init__(self):
            self.src = 0
            self.dest = 0

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

        self.edge = [self.Edge() for _ in range(edges)]


# main
# Create an object of Graph class
noVertices = 5
noEdges = 8
g = Graph(noVertices, noEdges)
# Create graph
g.edge[0].src = 1   # edge 1---2
g.edge[0].dest = 2

g.edge[1].src = 1   # edge 1---3
g.edge[1].dest = 3

g.edge[2].src = 1   # edge 1---4
g.edge[2].dest = 4

g.edge[3].src = 2   # edge 2---4
g.edge[3].dest = 4

g.edge[4].src = 2   # edge 2---5
g.edge[4].dest = 5

g.edge[5].src = 3   # edge 3---4
g.edge[5].dest = 4

g.edge[6].src = 3   # edge 3---5
g.edge[6].dest = 5

g.edge[7].src = 4   # edge 4---5
g.edge[7].dest = 5

for i in range(noEdges):
    print(f"{g.edge[i].src} - {g.edge[i].dest}")




# end time
endTime = time.perf_counter()
executionTime = (endTime - startTime) * 1000  # Convert to milliseconds

print("\nExecution Time: {:.4f} ms".format(executionTime))     
