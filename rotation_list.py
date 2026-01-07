"""
Given an array nums and an integer k, rotate the array to the right by k steps.
Right rotation means each element is shifted to a higher index; elements that “fall off” the end wrap to the front.
Example
nums = [1, 2, 3, 4, 5, 6, 7], k = 3
Move each item 3 steps to the right:
5 → front
6 → front (after 5)
7 → front (after 6)
Result: [5, 6, 7, 1, 2, 3, 4]
Think of it like cutting the last k elements and pasting them to the front.
"""




nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

for i in range(k):

    nums = [nums[-1]] + nums[:len(nums)-1]

print(nums)