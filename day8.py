input_filename = __file__.split('.')[0] + ".input"
with open(input_filename) as f:
    raw = f.read().strip().split('\n')


grid = [[int(cell) for cell in row] for row in raw]
assert all(len(row) == len(grid[0]) for row in grid) # all rows are the same length
max_x = len(grid) - 1
max_y = len(grid[0]) - 1


# class coord():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def neightbours(self):
#         result = []
#         pass


def neighbour_values(x, y):
    result = []
    if 0 <= x - 1:
        result.append(grid[x-1][y])
    if x + 1 <= max_x:
        result.append(grid[x+1][y])
    if 0 <= y - 1:
        result.append(grid[x][y-1])
    if y + 1 <= max_y:
        result.append(grid[x][y+1])
    return result


def part1():
    low_point_heights = []
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if all(cell < nv for nv in neighbour_values(x, y)):
                print(f"Low point {cell} at grid[{x}][{y}]")
                low_point_heights.append(cell)
    print(f"Found {len(low_point_heights)}")
    total_risk_level = sum(low_point_heights) + len(low_point_heights) # add 1 to each point to determine risk
    print(f"Sum of all risk levels: {total_risk_level}")


part1()
