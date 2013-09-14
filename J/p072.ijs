NB. this problem is very easy, once you've figured out the trick.
NB. /:~ ~. , %/~ (1+x:i.1e6) could also work, but there isn't enough memory in a
NB. normal computer.

totient =: (- ~:)&.q:
NB. solution (2+i.(1e6-1))
solution =: [: +/ totient