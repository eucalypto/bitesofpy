## [Bite 35. Having fun with heapq](https://codechalleng.es/bites/35/)

In this Bite you are provided with 3 data structures: a list of `int`s, a list of `datetime`s, and a list of `dict`s.

Complete the 3 functions to return the _largest n_ of each using `heapq` (our tests require this data `type` here).

Have fun and keep calm and code in Python!


## What I learned

The `heapq` package seems to sort (in place) lists into a heap form.

A heap is a binary tree where the two children of a node are smaller than the parent.

From this follows that the first element is the largest of the whole set.

There is also a sorting algorithm based on this fact and with the same name: heap sort.

The package `heapq` has also two functions:
`heapq.nlargest(n, iterable, key=None)` and `heapq.nsmallest(n, iterable, key=None)` that returns a list of n largest/smallest items in the list.

Nothing more was needed to solve this bite.
