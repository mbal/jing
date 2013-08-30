rot =: (1 |. ":)

NB. is y prime?
prime =: 1 = #@q:
NB. list of primes up to y
primes =: i.&.(p:^:_1)

main =: 3 : '+/ *./"1 prime@". (rot^:(1+i.6))"0 (primes y)'
