NB. According to mathworld wolfram, there's a formula to get the semiprimes
NB. under a given limit.

phi =: 13 : '+/(_1&p:@:>.@(y%p:)-]) i. _1&p:(%:y)'

NB. solution 1e8 = 17427258
solution =: phi