NB. copied from http://www.jsoftware.com/jwiki/Essays/Odometer
NB. odometer B B B computes all the numbers in base B with 3 digits
odometer =: #: i.@(*/)

NB. computes the exponents of the primes.
NB. the magic number 12 was computed by noting that the result should have
NB. about 14 prime factors. 13 and 14 produced results that were too high, so
NB. we lowered to 12.
exponents =: 1+2*(1 + odometer 12 $ 3)

NB. filters all the exponents which produce more than 8e6 divisors
filter =: exponents #"2~ (8e6 < */"1 exponents)

best =: 0 { filter
NB. solution best = 9350130049560600 
solution =: [: */ (x: @ (p:@i.@#) ^ x: @ |. &: (-:@<:))
 
