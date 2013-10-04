u =: 4 : '(900 - 3*y)*x^y-1'
s =: 3 : '+/ y&u"0 >:i.5000'

refine_guess =: 3 : 0
    m =. (+/ y) % 2
    v =. s m
    if. v > _6e11 do.
        m, 1 { y
    else.
        ({. y), m
    end.
)

NB. solution 1 1.2 = 1.002322108633 (0.64 secs)
NB. a larger interval for the bisection search would lead to
NB. longer execution time or death by too much memory used.
solution =: 0j12&":@(-:@+/@((refine_guess^:(-:@+/ > 1e_12"_))^:_))

