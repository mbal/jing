coeff =: 2, ,1,.(2+2*i.33),.1x
NB. ah, right association.
NB. `e 1 2 3` is equivalent to: `1 (+%) 2 (+%) 3`, where +% is the dyadic hook
NB. so, it evaluated as `1 + %2 + %3`, so: 1+%(2 + %3)
e =: (+%)/
NB. Once again, the tacit definition is very straight-forward, but it's ugly
NB. solution e coeff == 272
solution =: 3 : '+/ "."0 ": {. 2&x: y'
