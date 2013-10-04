NB. once solved p137 this is quite easy, since it's solved in the same way.
NB. The only difficult bit is getting the generating function for the 
NB. series. Here it is: (x+3x^2)/(1-x-x^2) = f(x)
NB. f(x) = n
NB. x+3xx = n(1-x-xx)
NB. delta = (n+1)^2 + 4(n+3)n = m^2 (should be a perfect square, in order
NB. for n to be rational).
NB. we get a lot of primitive solutions:
NB. (0, _1), (0, 1), (_3, _2), (_3, 2) (_4, _5), (_4, 5), (2, _7), (2, 7)
NB. but the method to solve is the same.

next =: (_14 _28) + (_9 _4 ,: _20 _9)&prod
prod =: +/ . *

get_sols2 =: (#~ 0&<)@:((0&{"1)@(next^:(<20)))

primitive =: (0 _1, 0 1, _3 _2, _3 2, _4 _5, _4 5, 2 _7 ,: 2 7)

NB. solution 30 = 5673835352990 (0.00088 secs)
solution =: 3 : '+/ x: (>:y) {. ~. /:~ ,/ get_sols2"1 primitive'
