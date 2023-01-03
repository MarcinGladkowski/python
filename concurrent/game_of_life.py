import asyncio

EMPTY = '-'
ALIVE = '*'


class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = []
        for _ in range(self.height):
            self.rows.append([EMPTY] * self.width)

    def get(self, y, x):
        return self.rows[y % self.height][x % self.width]

    def set(self, y, x, state):
        self.rows[y % self.height][x % self.width] = state

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.rows])


grid = Grid(5, 9)
grid.set(0, 2, ALIVE)
grid.set(1, 3, ALIVE)
grid.set(2, 3, ALIVE)
grid.set(2, 2, ALIVE)
grid.set(2, 1, ALIVE)

print('Init:')
print(grid)


def count_neighbors(y, x, get):
    n_ = get(y - 1, x + 0)
    ne = get(y - 1, x + 1)
    e_ = get(y + 0, x + 1)
    se = get(y + 1, x + 1)
    s_ = get(y + 1, x + 0)
    sw = get(y + 1, x - 1)
    w_ = get(y + 0, x - 1)
    nw = get(y - 1, x - 1)
    neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0

    for state in neighbor_states:
        if state == ALIVE:
            count += 1
    return count


def game_logic(state, neighbors):
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY
        elif neighbors > 3:
            return EMPTY
    else:
        if neighbors == 3:
            return ALIVE
    return state


async def step_cell(y, x, get, set):
    state = get(y, x)
    neighbors = count_neighbors(y, x, get)
    next_state = game_logic(state, neighbors)
    set(y, x, next_state)


async def simulate(grid):
    next_grid = Grid(grid.height, grid.width)
    tasks = []
    for y in range(grid.height):
        for x in range(grid.width):
            task = step_cell(y, x, grid.get, next_grid.set) # fan-out
            tasks.append(task)

    await asyncio.gather(*tasks) # fan-in

    return next_grid


print('Start')
for i in range(5):
    print('#' * 9)
    grid = asyncio.run(simulate(grid))
    print(grid)

print('Finish')