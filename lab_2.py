import random
from faker import Faker

faker = Faker()
iteration = 0
def can_place_cows(stalls, cows, min_dist):
    count = 1
    last_position = stalls[0]
    global iteration
    for position in stalls[1:]:
        if position - last_position >= min_dist:
            count += 1
            last_position = position
            if count == cows:
                return True
    iteration +=1
    return False

def largest_min_distance(N, C, stalls):

    low, high = 2, stalls[-1] - stalls[0]
    best = 2
    global iteration
    while low <= high:
        mid = (low + high) // 2
        if can_place_cows(stalls, C, mid):
            best = mid
            low = mid + 1
        else:
            high = mid - 1
        
        iteration += 1
    
    return best, iteration

def place_cows(stalls, C, min_dist):
    global iteration
    placed_cows = [stalls[0]]
    last_position = stalls[0]
    
    for position in stalls[1:]:
        if position - last_position >= min_dist:
            placed_cows.append(position)
            last_position = position
            if len(placed_cows) == C:
                break
    iteration += 1
    return placed_cows

def generate_cow_names(C):
    return [faker.first_name_female() for _ in range(C)]

N = 10 ** 5
C = random.randint(1, 10 ** 3)

def sorting(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = sorting(lst[:mid])
    right_half = sorting(lst[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_lst = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_lst.append(left[i])
            i += 1
        else:
            sorted_lst.append(right[j])
            j += 1

    sorted_lst.extend(left[i:])
    sorted_lst.extend(right[j:])
    return sorted_lst

free_sections = sorting(random.sample(range(1, N+1), N))

the_best_distance, iteration = largest_min_distance(N, C, free_sections)
placed_positions = place_cows(free_sections, C, the_best_distance)

print(f"Largest minimal distance: {the_best_distance}")
print(f"Number of iterations: {iteration}")

cow_names = generate_cow_names(C)
placed_cows = list(zip(placed_positions, cow_names))

while True:
    try:
        num_cows = int(input(f"Information about how many cows do you want to know? "))
        if 1 <= num_cows <= C:
            break
        else:
            print(f"Please enter a number from 1 to {C}.")
    except ValueError:
        print("Please enter an integer.")

for i, (position, name) in enumerate(placed_cows[:num_cows], 1):
    print(f"{i} cow: {name} in stall {position}")

with open("cows.py", "w", encoding="utf-8") as f:
    f.write("cows_data = [\n")
    for position, name in placed_cows:
        f.write(f"    ('{name}', {position}),\n")
    f.write("]\n")