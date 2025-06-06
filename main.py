def read_matrix_from_file(filename):
    with open(filename, 'r') as f:
        return [list(map(int, line.strip().split())) for line in f]

def count_islands(matrix):
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]

    def dfs(r, c):
        stack = [(r, c)]
        visited[r][c] = True
        while stack:
            x, y = stack.pop()
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                if (0 <= nx < rows and 0 <= ny < cols and
                        matrix[nx][ny] != 0 and not visited[nx][ny]):
                    visited[nx][ny] = True
                    stack.append((nx, ny))

    island_count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 0 and not visited[i][j]:
                dfs(i, j)
                island_count += 1

    return island_count

matrix = read_matrix_from_file('matrix.txt')
print(count_islands(matrix))