def longest_peaks(arr_peak):
    if len(arr_peak) < 3:
        return []
    
    n = len(arr_peak)
    all_peaks = [] 
    for i in range(1, n - 1):
        if arr_peak[i - 1] > arr_peak[i] < arr_peak[i + 1]:
            left = i - 1
            right = i + 1
            
            while left > 0 and arr_peak[left - 1] > arr_peak[left]:  
                left -= 1
            
            while right < n - 1 and arr_peak[right + 1] > arr_peak[right]:  
                right += 1
            
            peak_subsequence = arr_peak[left:right + 1]
            peak_length = right - left + 1 
            
            all_peaks.append((peak_length, peak_subsequence))
    
    return all_peaks

#arr_peak = [1, 3, 5, 4, 2, 8, 3, 7]
arr_peak = [-1, -10, -5, 7, 3, 5, 8, 9, 10, 0, 0, 1, 2, 3, 0]
all_peaks = longest_peaks(arr_peak)

print("LEVEL 3 RESULT:")
print("ALL Pits:")
for length, peak in all_peaks:
    print(f"Length: {length}, Pit: {peak}")