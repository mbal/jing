NB. we are looking for a multiple of q that shares its last digits with p
NB. (in the same order).
NB. N mod q = 0 (N = S + p)
NB. S + p mod q = 0
NB. s10^e + p mod q = 0
NB. s10^e = -p mod q
NB. ax = b mod n ==> x = ba^(phi(n)-1)
NB. phi(q) = q-1 ==> phi(q)-1 = q-2
NB. which is solved using: (q-p)*(10^e)^(q-2) mod q, where e is
NB. the number of digits in p


f =: 3 : 0
    'p q' =. y
    e =. >. 10^. p
    p + (10x^e) * q | (q - p) * (q&|@(10x&^)) (e*(q-2x))
)

NB. there are 78498 primes under 1e6
NB. solution 78497 = 18613426663617118 (6.25 secs)
solution =: 3 : '+/ f"1 (2 >\ p:2+i.y)'
