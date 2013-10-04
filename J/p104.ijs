pan =: '987654321'&-:@(\:~@":)
NB. last 10 digits of fibonacci
fibo =: 1e9&|@({: , +/)

NB. first ten digits of y-th fibonacci's number
NB. this version is much cleaner than its tacit equivalent
first10 =: 3 : 0
    phi =: -: >: %:5
    logf =: ((10^.phi)*y) - (-:10^.5)
    <. 10 ^ (8 + logf - <. logf)
)

NB. solution '' = 329468 (6.46 secs)
solution =: 3 : 0
    i =. 1
    prev =. 0 1
    while. (-. pan {: prev) +. -. pan first10 i do.
        prev =. fibo prev
        i =. >: i
    end.
    i
)

NB. this verb computes the next fibonacci number and its index
fibo2 =: >:@{. , 1e9&|@({: , +/@}.)
NB. solution2 1 0 1 = 3929468 (5.8 secs)
solution2 =: {.@(fibo2^:(-.@((pan@{:) *. pan@first10@{.))^:_)
