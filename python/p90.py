import itertools

numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '6')

c = 0
for d1 in itertools.combinations(numbers, 6):
    for d2 in itertools.combinations(numbers, 6):
        squares = ['01', '04', '06', '16', '25', '36', '46', '64', '81']
        for c1 in d1:
            for c2 in d2:
                if c1+c2 in squares:
                    squares.remove(c1+c2)
                if c2+c1 in squares:
                    squares.remove(c2+c1)
        if len(squares) == 0:
            c += 1
# Note: we count duplicates
# The die (0,1,2,3,4,5,6) is present both as first die and as second.
# So we can just divide by 2.
# I don't do any optimization even though the obvious one are:
# - at least dice must contain '0'
# - we don't need to check the duplicates
print c/2


