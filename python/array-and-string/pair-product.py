# pair product
# Write a function, pairProduct, that takes in an array and a target product as arguments.
# The function should return an array containing a pair of indices whose elements multiply
# to the given target. The indices returned must be unique.

# Be sure to return the indices, not the elements themselves.

# There is guaranteed to be one such pair whose product is the target.

def pairProduct(list, tar):
    print(list, tar)


# Examples:

print(pairProduct([3, 2, 5, 4, 1], 8))# -> [1, 3]
print(pairProduct([3, 2, 5, 4, 1], 10))# -> [1, 2]
print(pairProduct([4, 7, 9, 2, 5, 1], 5))# -> [4, 5]
print(pairProduct([4, 7, 9, 2, 5, 1], 35))# -> [1, 4]
print(pairProduct([3, 2, 5, 4, 1], 10))# -> [1, 2]
print(pairProduct([4, 6, 8, 2], 16))# -> [2, 3]
