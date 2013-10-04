NB. the solution to this problem is equivalent to the diophantine equation
NB. n^2 - 2*b^2 = -1
NB. A different approach leads to the approximation n/sqrt(2) for the number
NB. of blue discs. Which is a nice result, but not really useful in this
NB. situation.

NB. the solutions to the equation above can be found, from the primitive
NB. solution 1 1, using the map (x, y) -> (3x+2y-2, 4x+3y-3)
NB. (where x is the number of blue discs and y is the total number of discs)
NB. so, it is equivalent, using vector notation, to:
NB. 
NB. (x, y) -> (3 2) * (x) + (-2)
NB.           (4 3)   (y) + (-3)
NB. 
eqn =: (_2 _3) + (2 2 $ 3 2 4 3)&p 

NB. dot (inner) product
p =: +/ . *

NB. solution 1 1 = 756872327473 1070379110497 (0.00012 secs)
solution =: (eqn^:({: <: 1e12"_))^:_
