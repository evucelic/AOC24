from collections import deque

input_path = "input.txt"
input = []

with open(input_path, "r") as file:
    for line in file.readlines():
        input.append(line.strip())

visited = {}


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited.add(start)
    target = graph[start[0]][start[1]]

    while queue:
        current = queue.popleft()
        row, col = current

        for dx, dy in dirs:
            new_row, new_col = row + dx, col + dy
            if (
                0 <= new_row < len(graph)
                and 0 <= new_col < len(graph[0])
                and (new_row, new_col) not in visited
                and graph[new_row][new_col] == target
            ):
                visited.add((new_row, new_col))
                queue.append((new_row, new_col))

    return visited


def find_all_regions(input):
    n = len(input)
    m = len(input[0])

    visited = set()
    regions = []

    for i in range(n):
        for j in range(m):
            if (i, j) not in visited:
                region = bfs(input, (i, j))
                regions.append(region)
                visited.update(region)

    return regions


def fence(graph, region):
    l = 0
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for row, col in region:
        for dx, dy in dirs:
            new_row, new_col = row + dx, col + dy
            if (
                new_row < 0
                or new_row >= len(graph)
                or new_col < 0
                or new_col >= len(graph[0])
                or (new_row, new_col) not in region
            ):
                l += 1
    return l


regions = find_all_regions(input)

total = 0

for reg in regions:
    total += len(reg) * fence(input, reg)

print(total)
