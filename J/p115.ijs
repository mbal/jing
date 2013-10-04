NB. generalization of the solution to the previous problem.
NB. x is the minimum length of the block (m)
NB. y is the length of the row (n)
NB. It's not very nice, especially the G in the fork.
NB. ways == SUM(i=0, m/n, C(n+1 - (m-1)*i, 2i))
ways =: 4 : '+/ ((+: ! (y+1)&-&((x-1)&*)) (i. >. y % x))'

NB. solution i.200 = 168 (0.004 secs)
solution =: ({.@I.@:(1e6"_ < 50&ways"0))
