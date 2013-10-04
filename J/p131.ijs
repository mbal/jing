NB. n^3 + n^2p = n^2 (n+p) = k^3
NB. therefore, both n^2 and n+p must be cubes
NB. => x^3*y^3 = k^3
NB. p + n = y^3
NB. p = y^3 - z^3 = (y-z)(y^2+z^2+yz)
NB. since p is prime, one of (y-z) or (y^2+z^2+yz) must be 1.
NB. y - z = 1 ==> y = (z+1)
NB. p = (1+z)^2 + z^2 + (z+1)*z
NB.   = 1 + zz + 2z + zz + zz + z = 1 + 3z + 3zz

primes = p:i.1e6
f =: >:@(3&*)@(+ *:)

NB. solution 1e6 = 173 (0.0006 secs)
NB. find the upper bound using the equation 1+3z+3zz = y
bound =: 3 : '>. 1 { (#~ 0&<) , > p. ((>: - y), 3 3)'
solution =: #@((#~ (e.&primes *. 1e6&>))@f@i.@bound)
