NB. there isn't any prime 1-9 pandigital, since
NB. +/ i.10 = 45, which is divisible by 3, so all 9 digit pandigital are
NB. divisible by 3. This is true even for 8 digit pandigital.
NB. Therefore we are looking for 7 digits pandigital.

NB. solution = 7652413
solution =: >./ ((#~ (1&p:))@". ((i. ! 7) A. '1234567'))
