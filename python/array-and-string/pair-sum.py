# pair sum
# Write a function, pairSum, that takes in an array and a target sum as arguments.
# The function should return an array containing a pair of indices whose elements sum
# to the given target. The indices returned must be unique.

# Be sure to return the indices, not the elements themselves.

# There is guaranteed to be one such pair that sums to the target.


def pairSum(list, tar):
  # hash to store indices of previous numbers
  nums = {}

  for (i, num) in enumerate(list):
    complement = tar - num
    if complement in nums:
      return [nums[complement], i]
    nums[num] = i





# Examples:
print(pairSum([3, 2, 5, 4, 1], 8)); # [0, 2]
print(pairSum([4, 7, 9, 2, 5, 1], 5)); # [0, 5]
print(pairSum([4, 7, 9, 2, 5, 1], 3)); # [3, 5]
print(pairSum([1, 6, 7, 2], 13)); # [1, 2]
print(pairSum([9, 9], 18)); # [0, 1]
print(pairSum([6, 4, 2, 8 ], 12)); # [1, 3]
