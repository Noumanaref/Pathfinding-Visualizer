from queue import Queue
from queue import PriorityQueue

def get_neighbours(position, rows, cols, grid):

    row, col = position

    neighbours = []

    directions = [
        (-1, 0),  
        (1, 0),    
        (0, -1),   
        (0, 1)     
    ]

    for dr, dc in directions:

        new_row = row + dr
        new_col = col + dc

        if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols:

            if grid[new_row][new_col] == 0:

                neighbours.append((new_row, new_col))

    return neighbours



def bfs(grid, start, goal):

    rows = len(grid)
    cols = len(grid[0])

    queue = Queue()
    queue.put(start)

    visited = []
    frontier = []
    parent = {}

    visited.append(start)
    parent[start] = None

    while not queue.empty():

        current = queue.get()

        if current == goal:
            break

        neighbours = get_neighbours(current, rows, cols, grid)

        for neighbour in neighbours:

            if neighbour not in visited:

                visited.append(neighbour)

                parent[neighbour] = current

                queue.put(neighbour)
                if neighbour not in frontier:
                    frontier.append(neighbour)

    if goal not in parent:
        return None, visited, frontier

    path = []

    city = goal

    while city is not None:

        path.append(city)

        city = parent[city]

    path.reverse()

    return path, visited, frontier



def ucs(grid, start, goal):

    rows = len(grid)
    cols = len(grid[0])

    pq = PriorityQueue()

    pq.put((0, start))

    visited = []
    frontier = []

    parent = {}

    cost = {}

    parent[start] = None
    cost[start] = 0

    while not pq.empty():

        current_cost, current = pq.get()

        if current in visited:
            continue

        visited.append(current)

        if current == goal:
            break

        neighbours = get_neighbours(current, rows, cols, grid)

        for neighbour in neighbours:

            if neighbour not in visited:

                new_cost = current_cost + 1

                if neighbour not in cost or new_cost < cost[neighbour]:

                    cost[neighbour] = new_cost

                    parent[neighbour] = current

                    pq.put((new_cost, neighbour))
                    if neighbour not in frontier:
                        frontier.append(neighbour)

    if goal not in parent:
        return None, visited, frontier

    path = []

    city = goal

    while city is not None:

        path.append(city)

        city = parent[city]

    path.reverse()

    return path, visited, frontier



def greedy(grid, start, goal, heuristic):

    rows = len(grid)
    cols = len(grid[0])

    pq = PriorityQueue()

    pq.put((heuristic(start, goal), start))

    visited = []
    frontier = []

    parent = {}

    parent[start] = None

    while not pq.empty():

        h, current = pq.get()

        if current in visited:
            continue

        visited.append(current)

        if current == goal:
            break

        neighbours = get_neighbours(current, rows, cols, grid)

        for neighbour in neighbours:

            if neighbour not in visited:

                parent[neighbour] = current

                pq.put((heuristic(neighbour, goal), neighbour))
                if neighbour not in frontier:
                    frontier.append(neighbour)

    if goal not in parent:
        return None, visited, frontier

    path = []

    city = goal

    while city is not None:

        path.append(city)

        city = parent[city]

    path.reverse()

    return path, visited, frontier


def a_star(grid, start, goal,heuristic ):

    rows = len(grid)
    cols = len(grid[0])

    pq = PriorityQueue()

    pq.put((heuristic(start, goal), 0, start))

    visited = []
    frontier = []

    parent = {}

    cost = {}

    parent[start] = None
    cost[start] = 0

    while not pq.empty():

        f, g, current = pq.get()

        if current in visited:
            continue

        visited.append(current)

        if current == goal:
            break

        neighbours = get_neighbours(current, rows, cols, grid)

        for neighbour in neighbours:

            new_g = g + 1

            if neighbour not in cost or new_g < cost[neighbour]:

                cost[neighbour] = new_g

                parent[neighbour] = current

                h = heuristic(neighbour, goal)

                f = new_g + h

                pq.put((f, new_g, neighbour))
                if neighbour not in frontier:
                    frontier.append(neighbour)

    if goal not in parent:
        return None, visited, frontier

    path = []

    city = goal

    while city is not None:

        path.append(city)

        city = parent[city]

    path.reverse()

    return path, visited, frontier

