# uncompress

# Write a function, uncompress, that takes in a string as an argument.
# The input string will be formatted into multiple groups according to the
# following pattern:

# <number><char>

# for example, '2c' or '3a'.
# The function should return an uncompressed version of the string where each
# 'char' of a group is repeated 'number' times consecutively. You may assume
# that the input string is well-formed according to the previously mentioned
# pattern.

def uncompress(s):
  result = ''
  nums = '0123456789'
  multiple = ''

  for i in range(len(s)):
    if s[i] in nums:
      # print(s[i])
      multiple += s[i]
      # print(multiple, 'multiple')
      continue
    else:
      # print('not num', s[i])
      string = s[i];
      result += string * int(multiple)
      multiple = ''

  return result


# Examples:

# test_00:
print(uncompress("2c3a1t")); # 'ccaaat'
# test_01:
print(uncompress("4s2b")); # 'ssssbb'
# test_02:
print(uncompress("2p1o5p")); # 'ppoppppp'
# test_03:
print(uncompress("3n12e2z")); # 'nnneeeeeeeeeeeezz'
# test_04:
print(uncompress("127y")); #'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
