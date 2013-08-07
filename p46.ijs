

NB. It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
NB. 
NB. 9 = 7 + 2×12
NB. 15 = 7 + 2×22
NB. 21 = 3 + 2×32
NB. 25 = 7 + 2×32
NB. 27 = 19 + 2×22
NB. 33 = 31 + 2×12
NB. 
NB. It turns out that the conjecture was false.
NB. 
NB. What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

time =: 6!:2

primes =: p:@i.&(p:^:_1)

NB. these are trivially transformed into tacit form, but it requires too many
NB. caps and @.
help1 =: 3 : 'y +/ 2*(i.#y)^2'
helper =: 3 : '(i.y) -. ~. , (help1 primes y)'

solution =: 3 : '{. }. n #~ 1 <: (2 | n =: (helper y))'