def can_place_cows(stalls, cows, min_dist, return_positions=False):
    count = 1
    last_position = stalls[0]
    positions = [last_position]  
    for i in range(1, len(stalls)):
        if stalls[i] - last_position >= min_dist:
            count += 1
            last_position = stalls[i]
            positions.append(last_position)
            if count == cows:
                return (True, positions) if return_positions else True
    return (False, []) if return_positions else False


def largest_min_distance(N, C, free_sections):
    free_sections.sort()
    
    low, high = free_sections[0], free_sections[-1] - free_sections[0]
    best = 0
    
    while low <= high:
        mid = (low + high) // 2
        if can_place_cows(free_sections, C, mid):
            best = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return best


def get_placements(stalls, cows, min_dist):
    placements = []
    
    def backtrack(index, selected):
        if len(selected) == cows:
            placements.append(selected[:])
            return
        
        for i in range(index, len(stalls)):
            if not selected or stalls[i] - selected[-1] >= min_dist:
                selected.append(stalls[i])
                backtrack(i + 1, selected)
                selected.pop()

    backtrack(0, [])
    return placements


N = 5
C = 3
free_sections = [1, 2, 8, 4, 9]

best_distance = largest_min_distance(N, C, free_sections)

placements = get_placements(sorted(free_sections), C, best_distance)

print(f"Largest minimal distance: {best_distance}")
print("Possible placements of cows:")
for placement in placements:
    print(placement)
