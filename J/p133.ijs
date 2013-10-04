NB. a number p will never divide R(10^n) if A(p) has a factor different from 
NB. 2 or 5
A =: 10&mo"0
divides =: *./@:(2 5 e.~ q:)@A"0
primes =: i.&.(_1&p:) 1e5
NB. solution '' = 453647705 (1.55 secs)
solution =: 3 : '+/ primes -. (#~ divides) primes-.2 3 5'

NB. multiplicative order from Roger Hui's essay
NB. x mo y = n such that 1 = y | x^n
mo=: 4 : 0
 a=. x: x
 m=. x: y
 assert. 1=a+.m
 *./ a mopk"1 |: __ q: m
)

mopk=: 4 : 0
 a=. x: x
 'p k'=. x: y
 pm=. (p^k)&|@^
 t=. (p-1)*p^k-1  NB. totient
 'q e'=. __ q: t
 x=. a pm t%q^e
 d=. (1<x)+x (pm i. 1:)&> (e-1) */\@$&.> q
 */q^d
)
