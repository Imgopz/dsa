# Question
# An array is monotonic if it is either monotone increasing or monotone
# decreasing. An array is monotone increasing if all its elements from left to right
# are non-decreasing. An array is monotone decreasing if all its elements from
# left to right are non-increasing. Given an integer array return true if the given
# array is monotonic, or false otherwise.

# Clarifying Questions 
# Is an empty array monotonic? Yes
# Is an array with only 1 integer monotonic? Yes

# Test cases
# True
# [1,2,3] MI or ND
# [3,2,1] MD or NI 
# [1,2,2] ND
# [3,3,3] ND or NI
# [7] 
# []
# False
# [2,2,3,1]

def is_monotonic(arr):
    if len(arr) <= 1:
        return True  # Empty arrays and arrays with 1 element are monotonic
    
    increasing = decreasing = True
    
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            increasing = False
        if arr[i] > arr[i-1]:
            decreasing = False
        
        if not increasing and not decreasing:
            return False  # If it's neither increasing nor decreasing, it's not monotonic
    
    return True  # If we've made it through the loop, the array is monotonic

# Test cases
test_cases = [
    [1, 2, 2, 3],           # Monotone increasing
    [6, 5, 4, 4],           # Monotone decreasing
    [1, 3, 2],              # Not monotonic
    [1, 1, 1],              # Monotonic (both increasing and decreasing)
    [],                     # Empty array
    [5],                    # Single element array
    [1, 1, 2, 3, 3, 4],     # Monotone increasing
    [5, 4, 4, 3, 2, 2, 1]   # Monotone decreasing
]

for case in test_cases:
    print(f"Array {case} is {'monotonic' if is_monotonic(case) else 'not monotonic'}")