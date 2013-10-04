f =: (2x ^ [) * 5x ^ ]

gen_factors =: ~.@,@(f"0/~@(i.@>:@+:))

primitives =: 3 : 0
    res =: ,: 0$0
    for_a. gen_factors y do.
        ac =. (a + 10x^y)
        b =. (ac * 10x^y) % a
        if. b >: ac do.
            res =. res , (ac, b)
        end.
    end.
    res
) 

ndiv =: */ @: >: @: {: @: (__&q:) :: 0:

count_solutions =: 3 : '+/ ndiv"0 +./"1 primitives y'

NB. solution 1+i.9 = 53490 (0.031 secs)
solution =: +/@:(count_solutions"0)
