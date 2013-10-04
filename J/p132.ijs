NB. (10^n - 1)/9 = 0 (mod p) (p != 3)
NB. (10^n - 1) = 0 (mod p) 
NB. 10^n = 1 (mod p)

primes =: p:i.1e6

NB. solution 1e9 = 843296 (0.17 secs)
NB. I haven't found a way to make it tacit, since the residue/power verb
NB. doesn't work if the first parameter is a list
solution =: 3 : 0
    s =. 0
    c =. 0
    for_p. p:2+i.1e6 do.
        if. 1 = (p&|@(10&^)) y do.
            c =. >: c
            s =. s + p
        else.
        end.
        if. c >: 40 do.
            break.
        else.
        end.
    end.
    s
)
