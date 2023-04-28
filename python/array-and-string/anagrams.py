
# anagrams

# Write a function, anagrams, that takes in
# two strings as arguments. The function should
# return a boolean indicating whether or not the
# strings are anagrams. Anagrams are strings that
# contain the same characters, but in any oprintt_00:

def anagrams(s1, s2):
  if len(s1) != len(s2):
    return False
  count = {}

  for char in s1:
    if char not in count:
      count[char] = 1
    else:
      count[char] += 1

  for char in s2:
    if char not in count:
      return False
    else:
      count[char] -= 1

  for num in count:
    if count[num] != 0:
      return False

  return True


print(anagrams('restful', 'fluster')); # true
#test_01:

print(anagrams('cats', 'tocs')); # false
#test_02:

print(anagrams('monkeyswrite', 'newyorktimes')); # true
#test_03:

print(anagrams('paper', 'reapa')); # false
#test_04:

print(anagrams('elbow', 'below')); # true
#test_05:

print(anagrams('tax', 'taxi')); # false
#test_06:

print(anagrams('taxi', 'tax')); # false
#test_07:

print(anagrams('night', 'thing')); # true
#test_08:

print(anagrams('abbc', 'aabc')); # false
#test_09:

print(anagrams('po', 'popp')); # false
#test_10:

print(anagrams('pp', 'oo')) # false
