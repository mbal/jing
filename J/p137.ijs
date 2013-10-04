NB. another problem where we can reduce everything to a Pell's equation
NB. this time, we have four different primitive solutions:
NB. (-1, 0), (1, 0), (-2, -1), (2, -1). The next solutions can be found using:
next =: (_4 _2) + (_9 _20 ,: _4 _9)&prod
prod =: +/ . *

NB. well, I am going to leave it here, but it's not good J style.
NB. get_sols2 is much better (and faster -- about 5 five times faster).
get_sols =: 3 : 0
    s =. 0$0
    for_k. i.12 do.
        y =. next y
        if. 0 < (1 { y) do.
            s =. s , (1 { y)
        end.
    end.
    s
)

get_sols2 =: (#~ 0&<)@:((1&{"1)@(next^:(<12)))

NB. solution 15 = 1120149658760 (0.00012 secs). You can't get any faster
NB. than this (and using only 12 kb of memory).
solution =: 3 : 'y { ~. /:~ ,/ get_sols2"1 (_1 0, 1 0, _2 _1 ,: 2 _1)'
