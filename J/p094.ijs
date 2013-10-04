NB. the solutions are the solutions to the equation:
NB. a^2 = (a +- 1)^2/4 + h^2, where h is the height, and a is a side.
NB. after a bit of algebra, we reach:
NB. ((3a+-1)/2)^2 - 3h^2 = 1
NB. which is: x^2 - y^2 = 1, aka a Pell's equation.
NB. the primitive solution is given by a convergent of sqrt(3).
NB. solving gives: (1, 0) -- which is not a valid solution in this case, since
NB. h cannot be 0. The first real solution is (2, 1).
NB. successive solutions can be computed with the recurrence relation:
NB. (x, y) -> (2x + 3y, x + 2y)
NB. which is equivalent to:
next =: (2 3 ,: 1 2)&product
NB. where product is the inner product:
product =: +/ . *

NB. since we have both + and - in the formula, we'll handle the two cases
NB. separately.

NB. will handle the + sign
helper1 =: 3 : 0
    'xt yt' =. y
    (<:@+: xt) , yt * (xt - 2)
)

helper2 =: 3 : 0
    'xt yt' =. y
    (>:@+: xt) , yt (* +&2) xt
)

NB. solution 2 1 = 518408346 (0.0012 secs).
NB. this verb is really ugly, but I feel that a translation using Agenda
NB. could look even worse.
solution =: 3 : 0
    s =. 0
    t =. (helper1 y)
    while. 1e9 > 0 { t do.
        t =. (helper1 y)
        if. 1e9 < 0 { t do.
            break.
        end.
        if. (*./ t > 0) *. (*./ (0 = 3 | t)) do.
            s =. s + <: 0 { t
        end.
        t =. helper2 y
        if. (*./ t > 0) *. (*./ (0 = 3 | t)) do.
            s =. s + >: 0 { t
        end.
        y =. next y
    end.
    s
)
