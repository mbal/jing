NB. matrix product
dot =: +/ . *
poly =: dot~ %.

series =: 1 _1 1 _1 1 _1 1 _1 1 _1 1

evaluate =: p.

NB. this problem is very nice.
NB. sol series = 37076114526 (0.035 seconds)
solution =: 3 : 0
s =. 0
for_x. 1+i.10 do.
    ev =. y evaluate (x:1+i.(x+1))
    n =. }: ev
    t =. |."1 (1+i.x)^/(x:i.x)
    pol =. (|. (n poly t)) evaluate (1+i.(x+1))
    s =. s + +/ pol * 1- (ev = pol)
end.
s
)

fun =: (11 $ 1 _1)&p.
NB. fill the matrix with the coeff. of the equations
matrix =: (|."1 @ ((>:@i.@#) ^/ x:@i.@#))
NB. find the coefficients from the matrix (solve the simultaneous equations)
coeff =: |. @ (+/ .*~ %.) matrix
NB. find the first term which is wrong according to the sequence
NB. (the k+1 if the approximation is of k-th order)
fit =: coeff p. 1&+@#

NB. solution 1+x:i.10 = 37076114526 (0.04 secs)
solution2 =: [: +/ fit\@fun 