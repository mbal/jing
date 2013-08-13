NB. a(n) = (1/n)*Sum_{k=1..n} A008472(k)*a(n-k).
sopf =: +/@~.@q:
a =: 3 : '(% # y) * +/ y * (sopf >: i.-#y)'
a2 =: (% @ #) * (+/@ (* (sopf@>:@i.@-@#)))

NB. usage: `solution 1 0`
solution =: <: @ # @ ((, a2)^:(<&5000@{:)^:_)
