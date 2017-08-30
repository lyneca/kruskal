from node import Graph
string = """
8
15
0 1 0.732
0 3 0.134
0 4 0.112
1 4 0.770
2 5 0.379
2 6 0.984
2 7 0.577
3 4 0.642
3 6 0.763
3 7 0.589
4 5 0.473
4 7 0.334
5 6 0.748
5 7 0.544
6 7 0.474
4
0 1
3 6
2 6
2 5
""".strip()

arr = string.split('\n')
num_nodes = int(arr[0])
num_edges = int(arr[1])
num_mandatory = int(arr[num_edges+2])

# ^ The above code extracts the number of nodes, edges, and mandatory edges.
# In the actual code you would extract it from STDIN (using input() calls)

# Initialise our graph object
graph = Graph()

# for every line in the file from lines 2 to [num_edges + 2] (which is the
#  section containing the edges), add the edge to the graph object.
for line in arr[2:num_edges+2]:
    edge = (
        int(line.split()[0]),
        int(line.split()[1]),
        float(line.split()[2])
    )
    graph.add_edge(edge)

# For every line in the 'mandatory edges' section:
for line in arr[num_edges+3:num_edges+num_mandatory+3]:
    edge = (
        int(line.split()[0]),
        int(line.split()[1]),
    )
    # Find and select the edges inside the graph that correspond to the edge we just found
    graph.select([x for x in graph.edges if x[0] == edge[0] and x[1] == edge[1]][0])

    # Add the edge to the list of edges to ignore in the cycle checker
    graph.add_ignore(edge)

#######################
# KRUSKAL'S ALGORITHM #
#######################

# For every edge in the graph:
#     if we have already seen the edge:
#         skip the edge and continue to the next edge
#     if adding the edge to the graph does not create a cycle:
#         select the edge to be included in the MST

for edge in graph.edges:
    if edge in graph:
        continue
    if not graph.check_cycle(edge):
        graph.select(edge)

# If the number of edges in the MST is equal to the number of nodes - 1,
#  we have the right amount of edges in the MST.

if len(graph.selected_edges) == num_nodes - 1:
    print("Answer looks okay.")

# Print the sum of all the weightings. (sorry for all the list comprehensions I can't help it)
print(sum([x[2] for x in graph.selected_edges]))
