from typing import List


def count_consonants(s: str) -> int:
    """count the consonant"""
    count = 0

    for ch in s.lower():
        if ch.isalpha() and ch not in "aeiou":
            count+=1
    return count

print(count_consonants("hello"))
print(count_consonants("python3"))
print(count_consonants("AEIOU"))
print(count_consonants(" "))
print("\n")


#leetcode
def numJewelsInStones(jewels: str, stones: str) -> int:
    """return the numstone in jewel"""
    count = 0

    for ch in stones:
        if ch in jewels:
            count +=1
    return count

print(numJewelsInStones("z","ZZ"))


def sum_odd_numbers(nums: int) -> int:
    """sum the odd number of the list"""
    count = 0

    for num in nums:
        if num % 2 != 0:
            count +=num

    return count

print(sum_odd_numbers([1,2,3,4,5]))
print(sum_odd_numbers([]))
print(sum_odd_numbers([2,4,6]))



def repeat_count(s: str) -> dict:
    """return the dictionary with value"""

    dic = {}

    for ch in s:
        dic[ch] = dic.get(ch,0) + 1

    most_common =""
    max_count = 0


    for ch in dic:
        if dic[ch] > max_count:
            max_count = dic[ch]
            most_common = ch

    return most_common

print(repeat_count("hello"))

print("\n")



def smallest_number_than_current(nums: list) -> list:
    """how many numbers are smaller than current number"""
    numbers = []

    for i in range(len(nums)):
        count = 0
        current_num = nums[i]

        for j in range(len(nums)):
            if nums[j] < current_num:
                count +=1

        numbers.append(count)

    return numbers



print(smallest_number_than_current([8,1,2,2,3]))


def two_sum(nums: list[int], target: int) -> list[int]:
        seen = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement],i]
            seen[num] = i
        return []

print(two_sum([2,7,11,15],9))

def containsDuplicate(nums: list[int]) -> bool:
        

        seen = set()

        for i,num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            
        return False

print(containsDuplicate([1,2,3,1]))

def firstUniqChar(s: str) -> int:
        
        
        counter ={}

        for ch in s:
            counter[ch] = counter.get(ch,0) + 1

        for i,num in enumerate(s):
            if counter[num] == 1:
                
                return i
            
        return -1

print(firstUniqChar(""))


def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
        
        numbers =[]

        for i in range(len(nums)):
            count = 0
            current_num = nums[i]

            for j in range(len(nums)):
                if nums[j] < current_num:
                    count += 1

            numbers.append(count)
        return numbers


print(smallerNumbersThanCurrent([8,1,2,2,3]))


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
     """intersection the list of number """
     set1 = set(nums1)
     set2 = set(nums2)

     return list(set1 & set2)

print(intersection([],[]))

def validPalindrome(s: str) -> bool:
        word = ""

        for ch in s:
            if ch.isalnum():
                word += ch.lower()

        return word == word[::-1]
     

print(validPalindrome("A man, a plan, a canal: Panama"))


def removeDuplicates(nums: List[int]) -> int:
    left = 0

    for right in range(1, len(nums)):
        if nums[left] != nums[right]:
            left += 1
            nums[left] = nums[right]

    return left + 1

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


def moveZeores(nums: list[int]) -> None:
     """move zero in one side on list"""
     last_non_zero = 0

     for i in range(len(nums)):
          if nums[i] != 0:
            nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
            last_non_zero += 1



nums = [0,1,0,3,12]
moveZeores(nums)
print(nums)


def rearrangeArray(nums: List[int]) -> List[int]:
     negative_numbers = 1
     positive_numbers = 0
     result = [0]*len(nums)
     for num in nums:
          if num > 0:
               result[positive_numbers] = num
               positive_numbers += 2
          elif num < 0:
               result[negative_numbers] = num
               negative_numbers += 2
          
     return result



print(rearrangeArray([3,1,-2,-5,2,-4]))

def twoSum(numbers: List[int], target: int) -> List[int]:
        index = []

        for i,num in enumerate(numbers):
            current_sum = target - num
            for j in range(len(numbers)):
                if i !=j and numbers[j] == current_sum:
                    index.append(i)
                    index.append(j)
                    return index
        return []

print(twoSum([2,7,11,15],13))


def reverseString(s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
             s[left],s[right] = s[right],s[left]
             left += 1
             right -= 1



s =["h","e","l","l","o"]
reverseString(s)
print(s)

def numIdenticalPairss(nums: List[int]) -> int:
     count = 0

     for i in range(len(nums)):
          for j in range(i + 1,len(nums)):
               if nums[i] == nums[j]:
                    count += 1

     return count

print(numIdenticalPairss([1,2,3,1,1,3]))

def numIdenticalPairs(nums):
    seen = {}
    count = 0

    for num in nums:
        if num in seen:
            count += seen[num]
            seen[num] += 1
        else:
            seen[num] = 1

    return count
print(numIdenticalPairs([1,2,3,1,1,3]))


def numJewelsInStones(jewels: str, stones: str) -> int:
    """return the numstone in jewel"""
    jewels = set(jewels)
    count = 0

    for ch in stones:
         if ch in jewels:
              count += 1

    return count

print(numJewelsInStones("aA","aAAbbbb"))
print("\n")


def singleNumber(nums: List[int]) -> int:
     for i in range(len(nums)):
          current_num = nums[i]
          for j in range(len(nums)):
               if current_num == nums[j] and i != j:
                    break
          else:
            return nums[i]

        

print(singleNumber([1,2,1,4,2]))

def singleNumberdic(nums: list[int]) -> int:
     seen = {}

     for num in nums:
          if num in seen:
               seen[num] += 1

          else:
               seen[num] = 1
     for num,count in seen.items():
          if count == 1:
               return num

print(singleNumberdic([2,2,1]))

#letcode 268

def missingNumber(nums: List[int]) -> int:
     total = len(nums)+1
     #print(total)

     for i in range(total):
          current_num = i
          #print(current_num)
          for j in range(len(nums)):
               if current_num == nums[j]:
                    break
          else:
               return current_num
               
print(missingNumber([0,1]))

def missingNumberxor(nums: List[int]) -> int:
     
     number = 0

     for i in range(len(nums) + 1):
         
         number ^= i

     for num in nums:
         number ^= num

     return number



print(missingNumberxor([3,0,1]))

print("\n")

def majorityElement(nums: List[int]) -> int:
    total = len(nums) // 2

    for i in range(len(nums)):
        count = 0  # reset for each i

        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count += 1

        if count > total:
            return nums[i]

print(majorityElement([3,2,3]))

def majorityElementt(nums: List[int]) -> int:
    count = {}

    for num in nums:
        count[num] = count.get(num, 0) + 1

        if count[num] > len(nums) // 2:
            return num

print(majorityElementt([3,2,3]))

print("\n")

def isHappy(n: int) -> bool:
    seen = set()

    while n != 1:
        if n in seen:
            return False

        seen.add(n)

        total = 0
        for digit in str(n):
            total += int(digit) ** 2

        n = total

    return True
print(isHappy(211))

print("\n")
    
def canConstruct(ransomNote: str, magazine: str) -> bool:
     seen = {}
     seen1 = {}

     for ch in ransomNote:
          seen[ch] = seen.get(ch,0) + 1
     for ch in magazine:
          seen1[ch] = seen1.get(ch,0) + 1
     for ch in ransomNote:
          if seen[ch] > seen1.get(ch,0):
               return False
     return True



print(canConstruct("aaA","aaAb"))
print("\n")

def findTheDifference(s: str, t: str) -> str:
     count = {}

     for ch in s:
          count[ch] = count.get(ch,0) + 1
     for ch in t:
          if count.get(ch,0) == 0:
               return ch
          count[ch] -= 1

print(findTheDifference("a","aa"))

def findTheDifferencee(s: str, t: str) -> str:
     
     count = 0
     for ch in s:
          count ^= ord(ch)
     for ch in t:
          count ^= ord(ch)
     return chr(count)
     

print(findTheDifferencee("abcd","abcde"))
print("\n")

def isIsomorphic(s: str, t: str):

    if len(s) != len(t):
        return False

    count = {}
    count1 = {}

    for i in range(len(s)):

        ch1 = s[i]
        ch2 = t[i]

        if ch1 in count:
            if count[ch1] != ch2:
                return False
        else:
            count[ch1] = ch2

        if ch2 in count1:
            if count1[ch2] != ch1:
                return False
        else:
            count1[ch2] = ch1

    return True


print(isIsomorphic("paper", "title"))
print("\n")


def wordPattern(pattern: str, s: str) -> bool:
     t = s.split()
     if len(pattern) != len(t):
          return False
     seen = {}
     seen1 = {}
     for i in range(len(pattern)):
          ch1 = pattern[i]
          ch2 = t[i]

          if ch1 in seen:
               if seen[ch1] != ch2:
                    return False
          else:
            seen[ch1] = ch2

          if ch2 in seen1:
               if seen1[ch2] != ch1:
                    return False
          else:
               seen1[ch2] = ch1
     return True

print(wordPattern("abba","dog cat cat fish"))
print("\n")

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
     
     for i in range(len(nums)):
          for j in range(i+1,len(nums)):
               if nums[i] == nums[j]:
                    count = j - i 
                    if count <= k:
                         return True
     return False

print(containsNearbyDuplicate([1,2,3,1,2,3],2))

def containsNearbyDuplicatedict(nums: List[int], k: int) -> bool:
    count = {}

    for i, num in enumerate(nums):

        if num in count:
            if i - count[num] <= k:
                return True

        count[num] = i

    return False

print(containsNearbyDuplicatedict([1, 2, 3, 1], 3))

def maxProfit(prices: List[int]) -> int:
     max_profit = 0
     profit = 0

     for i in range(len(prices)):
          for j in range(i+1,(len(prices))):
               if prices[i] < prices[j]:
                    profit = prices[j] - prices[i]
               if max_profit < profit:
                    max_profit = profit

     return max_profit

print(maxProfit([7,1,5,3,6,4]))

def lengthOfLongestSubstring(s: str) -> int:
        seen = set() 
        left = 0 
        max_length = 0 
        for right in range(len(s)): 
            while s[right] in seen: 
                seen.remove(s[left]) 
                left += 1 
            seen.add(s[right]) 
            max_length = max(max_length, right - left + 1) 
        return max_length

print(lengthOfLongestSubstring("abcabcbbb"))
print("\n")




nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5

window_sum = sum(nums[:k])
average = window_sum / k
new = []
new.append(average)
for i in range(k,len(nums)):
     window_sum += nums[i] - nums[i - k]
     average = window_sum / k
     new.append(average)

print(new)

nums = [2, 3, 1, 2, 4, 3]
s = 7

left = 0
window_sum = 0
min_len = float('inf')          # "infinity" — no valid window found yet

for right in range(len(nums)):
    window_sum += nums[right]   # expand: add the new element

    while window_sum >= s:      # window is valid → try to shrink it
        min_len = min(min_len, right - left + 1)   # record current length
        window_sum -= nums[left]                   # remove leftmost element
        left += 1                                  # move left forward

if min_len == float('inf'):
    print(0)
else:
    print(min_len)

s = "eceba"
k = 2

left = 0
window = {} 
max_len = 0

for right in range(len(s)):
    
    window[s[right]] = window.get(s[right], 0) + 1

    
    while len(window) > k:
        window[s[left]] -= 1
        if window[s[left]] == 0:
            del window[s[left]]      
        left += 1

    
    max_len = max(max_len, right - left + 1)

print(max_len)

nums = [2, 7, 11, 15]
target = 9

left = 0 
right = len(nums) -1
num = []

while right > left:
     total = nums[left] + nums[right]
     if total == target:
          num.append(left+1)
          num.append(right + 1)
          break
     elif total < target:
          left += 1
     else:
          right -= 1
print(num)