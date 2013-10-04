helper =: 3 : 0
    rep =. 1
    c =. 1
    while. rep do.
        c =. >: c
        rep =. y | >: rep * 10
    end.
    c
)
A =: (0: ` helper)@.(1"_ = +.&10)

NB. solution '' = 149253
solution =: 3 : 0
    c =. 0
    i =. 7
    s =. 0
    primes =. p:i.1e5
    while. c < 25 do.
        if. -. i e. primes do.
            if. 0 = (A i) | (<: i) do.
                s =. s + i
                c =. >: c
            else.
            end.
        end.
        i =. i+2
    end.
    s
)
