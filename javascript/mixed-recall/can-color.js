/*

can color
Write a function, canColor, that takes in an object representing the adjacency list of an undirected graph. The function should return a boolean indicating whether or not it is possible to color nodes of the graph using two colors in such a way that adjacent nodes are always different colors.

For example, given this graph:

x-y-z

It is possible to color the nodes by using red for x and z,
then use blue for y. So the answer is true.

For example, given this graph:

    q
   / \
  s - r

It is not possible to color the nodes without making two
adjacent nodes the same color. So the answer is false.
test_00:
canColor({
  x: ["y"],
  y: ["x","z"],
  z: ["y"]
}); // -> true
test_01:
canColor({
  q: ["r", "s"],
  r: ["q", "s"],
  s: ["r", "q"]
}); // -> false
test_02:
canColor({
  a: ["b", "c", "d"],
  b: ["a"],
  c: ["a"],
  d: ["a"],
}); // -> true
test_03:
canColor({
  a: ["b", "c", "d"],
  b: ["a"],
  c: ["a", "d"],
  d: ["a", "c"],
}); // -> false
test_04:
canColor({
  h: ["i", "k"],
  i: ["h", "j"],
  j: ["i", "k"],
  k: ["h", "j"],
}); // -> true
test_05:
canColor({
  z: []
}); // -> true

test_06:
canColor({
  h: ["i", "k"],
  i: ["h", "j"],
  j: ["i", "k"],
  k: ["h", "j"],
  q: ["r", "s"],
  r: ["q", "s"],
  s: ["r", "q"]
}); // -> false
test_07:
canColor({
  "a": ["b", "d"],
  "c": ["b", "f"],
  "b": ["a", "c"],
  "d": ["a", "e"],
  "e": ["d", "f"],
  "f": ["e", "c"]
}); // -> true

*/
