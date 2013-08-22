NB. computes the number of divisors of y^2
ndiv2 =: */ @: >: @: +: @: {: @: (__&q:)

NB. the number of solutions is ((ndiv y^2)+1)/2,
NB. so, -: >: ndiv2 y
nsol =: -:@>:@ndiv2

NB. solution 1 = 180180 (1.2 secs)
solution =: (>:)^:(1000&>@nsol)^:_