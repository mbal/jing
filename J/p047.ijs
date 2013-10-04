NB. find all the 4-uple formed by consecutive numbers with 4 distinct 
NB. prime factors each.
s =: 4 (-:&(4 $ 4))\ #"1@~.@q:@(1+i.)
NB. solution 1e6 = 134042 (about 0.89 secs)
NB. lowering the bound to 1.4e5 gives the solution in 0.27 secs
solution =: 3 : '>: {. I. s y'
