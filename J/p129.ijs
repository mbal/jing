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

NB. solution 1e6 = 1000023 (6.5 secs)
NB. A(n) <: n, so it's useless to search for n < 1e6.
NB. as a (small) optimization we could only check for odd numbers
NB. because 10 +. n = gcd(10,n) = 1
solution =: (>:^:(A < 1e6"_))^:_
