NB. if x is a periodic rational, it can be written as p/(10^n - 1) where p is
NB. the recurring part and n is the length of said part. For example:
NB. 1/7 = 142857 / 999999
NB. So, when x is prime, we can compute n the same way we computed the fraction
NB. 142857/999999.
NB. while n % p > 0: n = 10 * n + 9; i++ ==> at the end, i contains the length

period =: 3 : 0
    n =. 9x
    i =. 1
    while. y | n do.
        n =. 9 + n * 10
        i =. i + 1
    end.
    i
)
NB. period diverges if y is a multiple of 2 or 5 (aka is not periodic)

helper =: (, period"0) @ p:@(3&+@i.@(_3&+@(p:^:_1)))

keys =: 1&{"1

NB. solution 1000 = 983 982 (list of (number, length)). (0.315 secs)
solution =: 3 : '_1 { (/: keys t) { [ t=.helper y'

period2 =: ((>:@])^:(0"_ < (| <:@(10x&^))))^:_
possible_sols =: p:@(3&+@i.@(_3&+@(p:^:_1)))
NB. solution2 1000 = 983 (0.36 secs)
solution2 =: 3 : 'p: 3 + (I. >./) (possible_sols y) (period2"0) 1'
