NB. the maximum solution to
NB. (a-1)^n + (a+1)^n mod a^2 is always F(a) = a*G(a) -- perfect
NB. occasion for a fork -- where G is the even number smaller than a:
NB. for example, F(4) = 4 * 2 = 8, while F(7) = 6*7 = 42

f =: * (<. &. -: @ <:)

NB. solution 3+i.998 = 33082500 (1 msec)
solution =: +/@f