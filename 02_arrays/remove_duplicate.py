"""
Problem: Remove duplicates from a list while preserving order.
Time Complexity: 0(n)
Space Complexity: 0(n)
"""
def remove_duplicates(nums):
    seen = set()         # Keep track of numbers we have encountered
    result = []          # This will store our ordered, unique numbers
    
    for num in nums:
        if num not in seen:
            seen.add(num)    # Mark as seen
            result.append(num) # Add to our result list to keep the order
            
    return result

# Test
nums = [1, 2, 2, 3, 1, 4]
print(remove_duplicates(nums)) # Output: [1, 2, 3, 4]