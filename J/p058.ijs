
NB. [: +/\ 1 , 4 # 2 * [: >: i.
NB. generate the corners of a spiral
H =: 4$ _1{ ]
F =: + (i.4)&*
J =: 3 : 'F (1 + %: _1 { y)'
NB. this verb generates only the next 4 numbers in the corners, from the previous.
corners4 =: J + H

prime =: 1 = #@q:
NB. returns the fraction of prime numbers in a list
pf =: (+/@prime) % #

display =: (1!:2) & 2
time =: 6!:2

NB. not very pretty, but it works
solution =: 3 : 0
x =. corners4 1
i =. 1
f =. 3
fr =. 1
l =. 5
while. fr > 0.5 do.
    i =. i + 1
    x =. corners4 x
    l =. l + 4
    f =. f + (+/@prime x)
    fr =. f % l
end.
i
)