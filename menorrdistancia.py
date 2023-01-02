class Graph:
    def __init__(self, vertices: int) -> None:
        """
        >>> graph = Graph(2)
        >>> graph.vertices
        2
        >>> len(graph.graph)
        2
        >>> len(graph.graph[0])
        2
        """
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def print_solution(self, distances_from_source: list[int]) -> None:
        """
        >>> Graph(0).print_solution([])  # doctest: +NORMALIZE_WHITESPACE
        Vertex 	 Distance from Source
        """
        print("Vertex \t Distance from Source")
        for vertex in range(self.vertices):
            print(vertex, "\t\t", distances_from_source[vertex])

    def minimum_distance(
        self, distances_from_source: list[int], visited: list[bool]
    ) -> int:
        """
        A utility function to find the vertex with minimum distance value, from the set
        of vertices not yet included in shortest path tree.

        >>> Graph(3).minimum_distance([1, 2, 3], [False, False, True])
        0
        """

        # Initialize minimum distance for next node
        minimum = 1e7
        min_index = 0

        # Search not nearest vertex not in the shortest path tree
        for vertex in range(self.vertices):
            if distances_from_source[vertex] < minimum and visited[vertex] is False:
                minimum = distances_from_source[vertex]
                min_index = vertex
        return min_index

    def dijkstra(self, source: int) -> None:
        """
        Function that implements Dijkstra's single source shortest path algorithm for a
        graph represented using adjacency matrix representation.

        >>> Graph(4).dijkstra(1)  # doctest: +NORMALIZE_WHITESPACE
        Vertex  Distance from Source
        0 		 10000000
        1 		 0
        2 		 10000000
        3 		 10000000
        """

        distances = [int(1e7)] * self.vertices  # distances from the source
        distances[source] = 0
        visited = [False] * self.vertices

        for _ in range(self.vertices):
            u = self.minimum_distance(distances, visited)
            visited[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.vertices):
                if (
                    self.graph[u][v] > 0
                    and visited[v] is False
                    and distances[v] > distances[u] + self.graph[u][v]
                ):
                    distances[v] = distances[u] + self.graph[u][v]

        self.print_solution(distances)


if __name__ == "__main__":
    graph = Graph(8)
    graph.graph = [
        [0, 675, 400, 166, 809, 720, 399, 233],
        [675, 0, 540, 687, 179, 348, 199, 401],
        [400, 540, 0, 107, 752, 521, 385, 280],
        [166, 687, 107, 0, 111, 540, 990, 361],
        [809, 179, 752, 111, 0, 206, 412, 576],
        [720, 348, 521, 540, 206, 0, 155, 621],
        [399, 199, 385, 990, 412, 155, 0, 100],
        [233, 401, 280, 361, 576, 621, 100, 0],
    ]
    print("Los vértices/caminos ideales son:")
    graph.dijkstra(0)

matrix = [
        [0, 675, 400, 166, 809, 720, 399, 233],
        [675, 0, 540, 687, 179, 348, 199, 401],
        [400, 540, 0, 107, 752, 521, 385, 280],
        [166, 687, 107, 0, 111, 540, 990, 361],
        [809, 179, 752, 111, 0, 206, 412, 576],
        [720, 348, 521, 540, 206, 0, 155, 621],
        [399, 199, 385, 990, 412, 155, 0, 100],
        [233, 401, 280, 361, 576, 621, 100, 0],
    ]



def minimum_cost_path(matrix: list[list[int]]) -> int:
    """
    Find the minimum cost traced by all possible paths from top left to bottom right in
    a given matrix

    >>> minimum_cost_path([[2, 1], [3, 1], [4, 2]])
    6

    >>> minimum_cost_path([[2, 1, 4], [2, 1, 3], [3, 2, 1]])
    7
    """

    # preprocessing the first row
    for i in range(1, len(matrix[0])):
        matrix[0][i] += matrix[0][i - 1]

    # preprocessing the first column
    for i in range(1, len(matrix)):
        matrix[i][0] += matrix[i - 1][0]

    # updating the path cost for current position
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1])

    return matrix[-1][-1]


print ("los km mínimos son:" ,minimum_cost_path(matrix))
if __name__ == "__main__":
    import doctest

    doctest.testmod()
