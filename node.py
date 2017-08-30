class DisjointSet:
    """
    Object to represent a disjoint set.
    """
    def __init__(self):
        # Initialise the dictionary of parents
        self.parent = {}

    def make_sets(self, a):
        # Takes in a list `a`, and creates initial parent mappings for each
        #  element in the list.
        # We set each element to be its own parent because at the start,
        #  each set contains only one element.
        for n in a:
            self.parent[n] = n

    def root(self, a):
        # Finds the root of an element in the set.
        # An element is a root if it is mapped to itself in the parent mapping,
        #  otherwise its mapping is its parent.
        if self.parent[a] == a:
            return a
        else: return self.root(self.parent[a])

    def union(self, a, b):
        # Finds the roots of two sets and merges them together.
        # Note that if you wanted to speed it up, you could make sure
        #  that the element with the more shallow tree is always added to that
        #  with the deeper tree.
        ra = self.root(a)
        rb = self.root(b)
        self.parent[ra] = rb

def rev(item):
    # Takes an edge and reverses its direction.
    #  (0, 1, 0.456) -> (1, 0, 0.456)
    return (item[1],item[0],item[2])

def is_cycle(graph):
    """
    Union Find algorithm for checking whether a Graph object has a cycle.
    """

    # Create a new disjoint set
    ds = DisjointSet()

    # Initialise the set's parent dictionary with the nodes of the graph
    ds.make_sets(graph.selected_nodes())

    # For every edge in the currently selected edges:
    for edge in graph.selected_edges:
        # If the edge is to be ignored (i.e. it's an element of A), skip it.
        if graph.is_ignored(edge):
            continue
        # Union find. If the root of the node on one side of the edge is the same as that of the other side,
        #  the nodes are in a cycle.
        if ds.root(edge[0]) == ds.root(edge[1]):
            return True
        # If they're not in a cycle, join (union) the two sides together in the disjoint set.
        else:
            ds.union(edge[0], edge[1])
    # If the program gets to this state, and hasn't returned true, the graph does not have a cycle.
    return False

class Graph:
    """
    Object to store a representation of a graph.
    """
    def __init__(self):
        # Initialise the graph.
        self.edges = []
        self.selected_edges = []
        self.ignore = []

    def edges(self, node):
        # Returns the edges that are connected to by a vertex
        return [x for x in self.edges if node in [x[0],x[1]]]

    def add_edge(self, edge):
        # Adds an edge to the graph.
        self.edges.append(edge)
    
    def select(self, edge):
        # Adds an edge to the MST.
        self.selected_edges.append(edge)

    def has_edge_to_node(self, node):
        # Returns true if the node is connected to any edges in the current MST.
        condition_list = [
            node in [x[0] for x in self.selected_edges],
            node in [x[1] for x in self.selected_edges],
        ]
        return any(condition_list)

    def check_cycle(self, edge):
        # Check whether adding an edge to the graph causes a cycle.
        # The algorithm for this is as follows:
        #  1. Create a temporary Graph object with the edge already added
        #  2. Check whether that graph has a cycle with is_cycle()

        # Make the temp graph
        temp_graph = Graph()

        # The temp graph's selected edges is all of our current selected edges plus the edge we're testing.
        temp_graph.selected_edges = self.selected_edges + [edge]  

        # Temp graph has the same ignore list as our current graph.
        temp_graph.ignore = self.ignore

        # Preliminary testing for efficiency.
        #  If the edge does not connect to any nodes currently in the MST, there's no way it could form a cycle.
        if not self.has_edge_to_node(edge[0]) or not self.has_edge_to_node(edge[1]):
            return False

        # Check whether the temp graph has a cycle.
        return is_cycle(temp_graph)

    def selected_nodes(self):
        # Looks through the selected edges and returns a list of all the selected nodes.
        return [x[0] for x in self.selected_edges] + [x[1] for x in self.selected_edges]

    def __contains__(self, item):
        # `graph.__contains__(item)` is called when you write `item in graph`.
        # I've implemented this so that `item in graph` returns whether the edge `item` is
        #  selected for the MST.
        return item in self.selected_edges or rev(item) in self.selected_edges
    
    def add_ignore(self, item):
        # Adds an item to the ignore list.
        self.ignore.append(item)

    def is_ignored(self, item):
        # Returns whether an item should be ignored by the cycle checker.
        if (item[0], item[1]) in self.ignore or (item[1], item[0]) in self.ignore:
            return True
        return False
