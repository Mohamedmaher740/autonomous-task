def count_treasures(grid, start_x, start_y):
    n = len(grid)
    m = len(grid[0])
    treasure_count = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    global visited
    visited = [[False] * m for _ in range(n)]

    def dfs(x, y):
        nonlocal treasure_count
        visited[x][y] = True
        print(grid[x][y])

        if grid[x][y] == 'T':
            treasure_count += 1

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < n and 0 <= ny < m ) and (not visited[nx][ny]) and (grid[nx][ny] != '#'):
                print(nx)
                print(ny)
                dfs(nx, ny)

    dfs(start_x, start_y)

    return treasure_count

n, m = map(int, input("Enter n and m: ").split())
grid = [input("Enter row: ") for _ in range(n)]
sx, sy = map(int, input("Enter starting x and y: ").split())

treasures = count_treasures(grid, sx, sy)
print("Total treasures collected:",treasures)
print(visited)