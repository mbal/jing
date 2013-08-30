NB. The fraction a/b closest to 3/7 is 3*(1e6/7) - 1
solution =: (3*(1e6 - 1)%7)-1

NB. Or, we can employ an optimization method, saying that
NB. a/b < 3/7 (therefore a < 3*b / 7), and iterating until
NB. the choice cannot be improved (a is the allowed integer
NB. closest to 3*b/7).
NB. Note that this is *almost* a fixed point search, but
NB. we cannot use ^:_ because the first argument to our
NB. helper doesn't depend on the outcome of the previous
NB. call of the function, but it's only related to how many
NB. iteration we've done. (We can put the number of iteration
NB. in the output of the function, but this is not very elegant)
load 'common.ijs'

solution2 =: 3 : 0
prev =. 0 1
for_i. (1e6 - i.1e6) do.
    prev =. i helper prev
end.
prev
)
        

helper =: 4 : 0
a =. <. (((3 * x) - 1) % 7)
if. (((1 { y) * a) > ((0 { y) * x)) do.
    new =. a, x, 0$0
else.
    new =. y
end.
new
)
     
     