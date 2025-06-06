def read_data_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    cities = []
    storages = []
    pipelines = []

    section = None

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line.startswith("cities:"):
            section = 'cities'
            cities = [c.strip() for c in line.split(":")[1].split(',')]
        elif line.startswith("storages:"):
            section = 'storages'
            storages = [s.strip() for s in line.split(":")[1].split(',')]
        elif line.startswith("pipelines:"):
            section = 'pipelines'
        elif section == 'pipelines':
            if '->' in line:
                frm, to = [p.strip() for p in line.split('->')]
                pipelines.append([frm, to])

    return cities, storages, pipelines


def check_gas_supply(cities, storages, pipelines):
    graph = {node: [] for node in set(cities + storages)}
    for frm, to in pipelines:
        graph[frm].append(to)

    def dfs(start, visited):
        stack = [start]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                for neighbor in graph.get(current, []):
                    stack.append(neighbor)

    result = []

    for storage in storages:
        visited = set()
        dfs(storage, visited)
        unreachable = [city for city in cities if city not in visited]
        if unreachable:
            result.append([storage, unreachable])

    return result


try:
    cities, storages, pipelines = read_data_from_file('data.txt')
except FileNotFoundError:
    print("Error: The file 'data.txt' was not found.")
    exit(1)
except ValueError as e:
    print(f"Error: Invalid data format - {e}")
    exit(1)

result = check_gas_supply(cities, storages, pipelines)

if result:
    print("Gas supply issues detected:")
    for storage_name, unreachable_cities in result:
        print(f"Storage '{storage_name}' cannot supply gas to: {', '.join(unreachable_cities)}")
else:
    print("All cities are reachable from the storages.")
