# Question

# You are given an array of Integers in which each subsequent value is not less
# than the previous value. Write a function that takes this array as an input and
# returns a new array with the squares of each number sorted in ascending
# order.

# Clarifying Questions

# Are all numbers positive?
# Are the Integers distinct?
# Can an empty array of Integers be given as input?

# Test cases 
# different I/Ps and expected O/Ps
# Can form together with the team
# eg. [1,3,5] => [1,9,25]
# eg. [0,5,6] => [0,25,36]
# eg. [-4,-2,0,1,3] => [16,4,0,1,9] => [0,1,4,9,16]
# eg. [2,3,3] => [4,9,9]

def sorted_squared_array(arr):
    n = len(arr)
    result = [0] * n  # Initialize result array with zeros
    left, right = 0, n - 1  # Set pointers at the start and end of the array
    
    # Traverse the array from right to left
    for i in range(n - 1, -1, -1):
        # Compare absolute values of elements at left and right pointers
        if abs(arr[left]) > abs(arr[right]):
            result[i] = arr[left] ** 2  # Square and place the left element
            left += 1  # Move left pointer to the right
        else:
            result[i] = arr[right] ** 2  # Square and place the right element
            right -= 1  # Move right pointer to the left
    
    return result

# Test cases
test_cases = [
    [1, 3, 5],
    [0, 5, 6],
    [-4, -2, 0, 1, 3],
    [2, 3, 3],
    []  # Edge case: empty array
]

for case in test_cases:
    print(f"Input: {case}")
    print(f"Output: {sorted_squared_array(case)}")
    print()

# Detailed walkthrough of the algorithm:
# 
# 1. Initialize variables:
#    - n: length of the input array
#    - result: a new array of the same length, filled with zeros
#    - left: pointer starting at the beginning of the array (index 0)
#    - right: pointer starting at the end of the array (index n-1)
#
# 2. Iterate through the array from right to left (i from n-1 to 0):
#    This is because we're filling the result array from largest to smallest.
#
# 3. Compare absolute values of arr[left] and arr[right]:
#    - We use absolute values because negative numbers, when squared, 
#      can become larger than positive numbers.
#
# 4. Square the larger value and place it in result[i]:
#    - If abs(arr[left]) is larger, square arr[left] and move left pointer right
#    - If abs(arr[right]) is larger or equal, square arr[right] and move right pointer left
#
# 5. Repeat steps 3-4 until all elements are processed
#
# 6. Return the result array, which is now filled with squared values in ascending order
#
# This algorithm works because:
# - The input array is sorted (each subsequent value is not less than the previous)
# - The largest squared values will always be at the ends of the array
# - By comparing absolute values, we handle both positive and negative numbers correctly
#
# Time complexity: O(n) - we traverse the array once
# Space complexity: O(n) - we create a new array of the same length as the input

# Now, let me elaborate on some key points:

# Two-pointer technique:
# We use two pointers (left and right) to compare elements from both ends of the array. This is efficient because we know the largest squared values will be at the ends of the sorted input array.
# Absolute value comparison:
# We compare absolute values because negative numbers, when squared, can be larger than positive numbers. For example, -4 squared is 16, which is larger than 3 squared (9).
# Building the result array backwards:
# We fill the result array from right to left (largest to smallest) because it's easier to determine the largest squared value at each step.
# Handling edge cases:

# The algorithm naturally handles empty arrays (the loop won't execute).
# It correctly processes arrays with duplicate values.
# It works for arrays containing negative numbers, zero, and positive numbers.


# Time and space complexity:

# Time complexity is O(n) because we process each element once.
# Space complexity is O(n) for the result array. We don't use any additional space that scales with input size.


# In-place vs. new array:
# We create a new array rather than modifying the input in-place. This is often preferred as it doesn't alter the original data.


# Brute force method

def sorted_squared(array):
    n = len(array)
    res = [0] * n

    for i in range(n):
        res[i] = array[i] ** 2
    
    res.sort()

    return res

for case in test_cases:
    print(f"Input: {case}")
    print(f"Output: {sorted_squared(case)}")
    print()
