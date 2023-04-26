# five sort

# Write a function, fiveSort, that takes in an array of numbers as an argument.
# The function should rearrange elements of the array such that all 5s appear
# at the end. Your function should perform this operation in-place by mutating
# the original array. The function should return the array.

# Elements that are not 5 can appear in any order in the output,
# as long as all 5s are at the end of the array.

def fiveSort(a):
  i = 0
  j = len(a) - 1

  while i < j:
    if a[j] == 5:
      j -= 1
    elif a[i] == 5:
      a[i], a[j] = a[j], a[i]
    else:
      i += 1

  return a

# Examples
# test_00
print(fiveSort([12, 5, 1, 5, 12, 7]));
# [12, 7, 1, 12, 5, 5]
# test_01
print(fiveSort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5]));
# [2, 2, 10, 6, 1, 5, 5, 5, 5, 5]
# test_02
print(fiveSort([5, 5, 5, 1, 1, 1, 4]));
# [4, 1, 1, 1, 5, 5, 5]
# test_03
print(fiveSort([5, 5, 6, 5, 5, 5, 5]));
# [6, 5, 5, 5, 5, 5, 5]
# test_04
print(fiveSort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5]));
# [4, 1, 2, 1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 5]
# test_05
fives = [5] * 2000;
fours = [4] * 2000;
nums = [*fives, *fours]
print(fiveSort(nums))
# twenty-thousand 4s followed by twenty-thousand 5s
# [4, 4, 4, 4, ..., 5, 5, 5, 5]
