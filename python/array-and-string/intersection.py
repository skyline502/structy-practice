# intersection

# Write a function, intersection, that takes in two arrays, a,b, as arguments.
# The function should return a new array containing elements that are in both of the two arrays.

# You may assume that each input array does not contain duplicate elements.

def intersection(a1, a2):
  result = []

  for el in a1:
    if el in a2:
      result.append(el)

  return result


# Examples:

print(intersection([4,2,1,6], [3,6,9,2,10])) # [2,6]
print(intersection([2,4,6], [4,2])) # [2,4]
print(intersection([4,2,1], [1,2,4,6])) # [1,2,4]
print(intersection([0,1,2], [10,11])) # []

a = [];
b = [];
for i in range(50000):
  a.append(i);
  b.append(i);

print(intersection(a, b)) # [0,1,2,3,..., 49999]
