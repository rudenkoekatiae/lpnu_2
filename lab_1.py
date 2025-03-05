#level 1

nums_1 = [-4,-2,0,1,3]
nums_2 = [1,2,3,4,5]

def square(lst):
    return sorted([i**2 for i in lst])

squared_list1 = sorted(square(nums_1))
squared_list2 = sorted(square(nums_2))
print(f"LEVEL 1 RESULT: \n FIRST SQUARED LIST : {squared_list1},\n SECOND SQUARED LIST: {squared_list2}\n")

#level 2

def find_kth_largest(arr, k):
    if len(arr) < k:
        return "ERROR. The array contains less elemnets than k"
    
    sorted_arr_kth = sorted(arr_kth, reverse=True)
    
    kth_largest = sorted_arr_kth[k - 1]
    
    index = arr.index(kth_largest)
    
    return kth_largest, index

arr_kth = [15, 7, 22, 9, 36, 2, 42, 18]
k = 3

result = find_kth_largest(arr_kth, k)
if isinstance(result, str):
    print(result)
else:
    kth_largest, index = result
    suffix = "th"
    if k % 10 == 1 and k % 100 != 11:
        suffix = "st"
    elif k % 10 == 2 and k % 100 != 12:
        suffix = "nd"
    elif k % 10 == 3 and k % 100 != 13:
        suffix = "rd"
    
    print(f"LEVEL 2 RESULT \n The {k}{suffix} largest element: {kth_largest}")
    print(f" The position of {k}{suffix} largest element in array: {index}\n")
#level 3

def longest_peak(arr_peak):
    if len(arr_peak) < 3:
        return 0
    
    max_length = 0
    n = len(arr_peak)
    
    for i in range(1, n - 1):

        if arr_peak[i - 1] < arr_peak[i] > arr_peak[i + 1]:
            left = i - 1
            right = i + 1
            
            while left > 0 and arr_peak[left - 1] < arr_peak[left]:
                left -= 1
            
            while right < n - 1 and arr_peak[right + 1] < arr_peak[right]:
                right += 1
            
            max_length = max(max_length, right - left + 1)
    
    return max_length
arr_peak = [1, 3, 5, 4, 2, 8, 3, 7]
the_longest_peak = longest_peak(arr_peak)

print(f"LEVEL 3 RESULT: \n THE LONGEST PEAK: {the_longest_peak}") 
