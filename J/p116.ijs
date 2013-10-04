NB. we can try some code very similar to p114. However, in this case
NB. I prefer to try a combinatoric solution (like solution2 in p114)

NB. it's almost identical to the verb in solution2 in p114, but we need
NB. two parameters to represent a tiling.
NB. Can be transformed in tacit form? Probably.
f =: 4 : 0
    s =. 0
    for_k. >:i.<.(y % x) do.
        s =. s + k ! (k + y - k * x)
    end.
    s
)

NB. solution 50 = 20492570929 (0.0005 secs)
solution =: +/@((2 3 4)&(f"(0 0 0)))
    
