# most frequent char

# Write a function, mostFrequentChar, that takes in a string as
# an argument. The function should return the most frequent character
# of the string. If there are ties, return the character that appears
# earlier in the string.

# You can assume that the input string is non-empty.

def mostFrequentChar(s):
  count = {}

  for char in s:
    if char not in count:
      count[char] = 1
    else:
      count[char] += 1

  mostFrequent = 0
  result = None
  for char in count:
    if count[char] > mostFrequent:
      mostFrequent = count[char]
      result = char

  return result

# Examples:


print(mostFrequentChar('bookeeper')); # 'e'

print(mostFrequentChar('david')); # 'd'

print(mostFrequentChar('abby')); # 'b'

print(mostFrequentChar('mississippi')); # 'i'

print(mostFrequentChar('potato')); # 'o'

print(mostFrequentChar('eleventennine')); # 'e'

print(mostFrequentChar("riverbed")); # 'r'
