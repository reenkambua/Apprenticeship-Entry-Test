# Write a function that returns the second-largest number in a given list of integers.

def second_largest(nums):
    unique_nums = list(set(nums))  # remove duplicates
    unique_nums.sort(reverse=True) #Sort in descending order
    if len(unique_nums) < 2:
        return None  # no second largest
    return unique_nums[1]

# Example
print(second_largest([4, 1, 7, 3, 7, 9, 9, 5])) 


