NB. sigma(x) = Sum(a(i) + 1) where a(i) is the number of i in the prime
NB. factorization. For example:
NB. 12 = 2 * 2 * 3 ==> a(2) = 2, a(3) = 1
NB. therefore, sigma(12) = 3*2 = 6
sigma =: */@:>:@(1&{"2)@(__&q:)

triangle =: (((, (_1&{ + #))^:(sigma@(_1&{) < 500"_)))^:_

NB. solution 0 1 = 76576500 (0.3 secs)
solution =: _1&{@triangle

NB. solution2 15e3 = 76576500 (0.16 secs), but the upper bound must
NB. be guessed before (or refined after some run), because it scales
NB. really badly (raising the bound to 1e5 gives the solution in 11 secs)
solution2 =: {.@:(#~ (500"_ < sigma))@:(+/\@:>:@i.)
