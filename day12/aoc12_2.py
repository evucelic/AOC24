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


def sides(graph, region):
    corners = 0
    n = len(graph)
    m = len(graph[0])

    for tup in region:
        row, col = tup

        bottom = (row + 1, col) if row + 1 < n else None
        top = (row - 1, col) if row - 1 >= 0 else None
        right = (row, col + 1) if col + 1 < m else None
        left = (row, col - 1) if col - 1 >= 0 else None

        # Bottom left corner
        if (bottom not in region or bottom is None) and (
            left not in region or left is None
        ):
            corners += 1

        # Bottom right corner
        if (bottom not in region or bottom is None) and (
            right not in region or right is None
        ):
            corners += 1

        # Top right corner
        if (top not in region or top is None) and (
            right not in region or right is None
        ):
            corners += 1

        # Top left corner
        if (top not in region or top is None) and (left not in region or left is None):
            corners += 1

        # concave corners
        if bottom in region and left in region:
            bottom_left = (row + 1, col - 1)
            if bottom_left not in region and 0 <= row + 1 < n and 0 <= col - 1 < m:
                corners += 1

        if bottom in region and right in region:
            bottom_right = (row + 1, col + 1)
            if bottom_right not in region and 0 <= row + 1 < n and 0 <= col + 1 < m:
                corners += 1

        if top in region and right in region:
            top_right = (row - 1, col + 1)
            if top_right not in region and 0 <= row - 1 < n and 0 <= col + 1 < m:
                corners += 1

        if top in region and left in region:
            top_left = (row - 1, col - 1)
            if top_left not in region and 0 <= row - 1 < n and 0 <= col - 1 < m:
                corners += 1

    return corners


regions = find_all_regions(input)

total = 0

for reg in regions:
    total += len(reg) * sides(input, reg)

print(total)
