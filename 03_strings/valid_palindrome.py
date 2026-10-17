"""
LeetCode 125: Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/
Difficulty: Easy
Time Complexity: 0(n)
Space Complexity: 0(n)
"""


def valid_palindrome_optimized(s):
    cleaned = []
    for letter in s:
        if letter.isalnum():
            cleaned.append(letter.lower())
            
    new_text = "".join(cleaned)  # Fast O(n) joining
    return new_text == new_text[::-1]
