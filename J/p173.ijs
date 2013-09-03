NB. doesn't work. Too slow.
divisors =: (2+i.@-:) #~ (0 = ((2+i.@-:) | ]))
divisors2 =: (,. |.) @ divisors
heven =: #~ */"1@(~:/"1 *. 0=2&|)
tiling =: (<.@-:@#@heven@divisors2)

NB. smarter solution.
NB. solution 1e6 = 1572729 (istantaneous)
solution =: 3 : '+/ (<. y % (4 * t)) - t=:1+i.<.(-: >: %: >: y)'

