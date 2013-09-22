div =: /:~ @: , @: > @: (*/&.>/) @: ((^ i.@>:)&.>/) @: (__&q:)
d =: +/@div - [

NB.           zeroes numbers |      all numbers
NB.            with d(a) = a |   that have d(a) = d(b),
NB.                          |   (note that a could be equal to b)
solution =: +/@(* (~: d"0))  @  (#~ (= (d^:2)"0))
