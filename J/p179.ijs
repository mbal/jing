NB. computes the number of divisors of y^2
ndiv =: */ @: >: @: {: @: (__&q:)
NB. I opted for the simplest solution possible. (create a list with the
NB. the number of divisors of all the numbers, group them 2 by 2, check
NB. if equal, then sum).
NB. solution 1e7 = 986262 (quite slow)
solution =: 3 : '+/ (=/"1 (2 ndiv"0\ (2+i.(y-1))))'