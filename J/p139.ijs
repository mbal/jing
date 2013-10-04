NB. a^2 + b^2 = c^2 with b = a-d
NB. aa + (a-d)^2 = ddyy (c = dy)
NB. after a bit of algebra, we reach this:
NB. (2a+d)^2 + d^2 = 2d^2y^2
NB. which is a Pell's equation in disguise:
NB. setting x=(2a+d)/d gives:
NB. x^2 - 2y^2 = -1
NB. which is solved by the primitive (1, 1) and the recurrence relation:
next =: (3 4 ,: 2 3)&prod
prod =: +/ . *

get_sols =: ((, next@{:)^:(+/@{: < 1e8"_))^:_

NB. 7 5 is the primitive solution (1 1 is not valid, in this setting).
NB. solution ,: 7 5 = 10057761 (80 microsecs)
solution =: 3 : '+/ x: <. 1e8 % +/"1 get_sols y'
