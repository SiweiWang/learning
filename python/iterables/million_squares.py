"""demo of the generator """
miilion_squares= (x*x for x in range(1, 1000001))

# right now the value is not evaluated yet

miilion_squares
print(miilion_squares)

# We can force the result by using list, following will return list of 1000000 numbers
print((list(miilion_squares)))

# note that generate is only eval oncem, following will retunr []
print(list(miilion_squares))

# now let's compute the sum of the first 1000000 squares, note that the sum function call does not another pair of brackets
print(sum(x*x for x in range(1, 1000001)))
