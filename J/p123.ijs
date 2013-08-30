NB. as hk proved in project euler's forum for problem 120, if
NB. n is even, the remainder for the formula (k+1)^ n + (k-1)^n mod k^2 is
NB. 2(n+1) * k. In this case, k = p:n
f =: (+:@>: * p:)

solution =: >: @: ((2&+^:(1e10&>@f))^:_)