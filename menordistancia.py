import heapq
graph = [
    [0, 1, 6, 3, 7, 5, 1, 7, 4, 2],
    [1, 0, 8, 1, 3, 7, 3, 6, 7, 2],
    [2, 1, 0, 6, 5, 1, 1, 3, 2, 8],
    [3, 6, 9, 0, 9, 3, 1, 5, 6, 9],
    [7, 4, 6, 3, 0, 1, 7, 1, 1, 1],
    [1, 3, 1, 9, 1, 0, 8, 1, 3, 7],
    [1, 3, 5, 9, 9, 1, 0, 4, 2, 1],
    [3, 1, 2, 5, 4, 2, 1, 0, 3, 9],
    [1, 2, 9, 3, 1, 3, 8, 5, 0, 1],
    [2, 3, 1, 1, 9, 4, 4, 5, 8, 0],
]

def find_shortest_paths(graph, start_point):
    # initialize graphs to track if a point is visited,
    # current calculated distance from start to point,
    # and previous point taken to get to current point
    visited = [[False for col in row] for row in graph]
    distance = [[float('inf') for col in row] for row in graph]
    distance[start_point[0]][start_point[1]] = 0
    prev_point = [[None for col in row] for row in graph]
    n, m = len(graph), len(graph[0])
    number_of_points, visited_count = n * m, 0
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    min_heap = []

    # min_heap item format:
    # (pt's dist from start on this path, pt's row, pt's col)
    heapq.heappush(min_heap, (distance[start_point[0]][start_point[1]], start_point[0], start_point[1]))

    while visited_count < number_of_points:
        current_point = heapq.heappop(min_heap)
        distance_from_start, row, col = current_point
        for direction in directions:
            new_row, new_col = row + direction[0], col + direction[1]
            if -1 < new_row < n and -1 < new_col < m and not visited[new_row][new_col]:
                dist_to_new_point = distance_from_start + graph[new_row][new_col]
                if dist_to_new_point < distance[new_row][new_col]:
                    distance[new_row][new_col] = dist_to_new_point
                    prev_point[new_row][new_col] = (row, col)
                    heapq.heappush(min_heap, (dist_to_new_point, new_row, new_col))
        visited[row][col] = True
        visited_count += 1

    return distance, prev_point 

def find_shortest_path(prev_point_graph, end_point):
    shortest_path = []
    current_point = end_point
    while current_point is not None:
        shortest_path.append(current_point)
        current_point = prev_point_graph[current_point[0]][current_point[1]]
    shortest_path.reverse()
    return shortest_path

