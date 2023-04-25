# ##
# compress
# Write a function, compress, that takes in a string as an argument. The function should return a compressed version of
# the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed
# by the character. Single character occurrences should not be changed.

# 'aaa' compresses to '3a'
# 'cc' compresses to '2c'
# 't' should remain as 't'
# You can assume that the input only contains alphabetic characters.


def compress(s):
  print(s)


# Examples
# test_00:
print(compress('ccaaatsss')); # '2c3at3s'
# test_01:
print(compress('ssssbbz')); # '4s2bz'
# test_02:
print(compress('ppoppppp')); # '2po5p'
# test_03:
print(compress('nnneeeeeeeeeeeezz')); # '3n12e2z'
# test_04:
print(compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'));
# '127y'
