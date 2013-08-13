load 'common.ijs'
ways =: 4 : 0 M.
    NB. x is the number to decompose, y is the (sorted) list.
    if. x = 0 do.
        1
    elseif. x < 0 do.
         0
    elseif. 0 = #y do.
        0
    elseif. 1 do.
        (x ways }. y) + ((x - {.y) ways y)
    end.
)

NB. tacit equivalent to the previous one, but runs much faster
ways2 =: 0:`1:`(0:` (([ $: }.@:]) + (([-{.@]) $: ])) @. (0: < #@:]))@.(1:+*@[) 
NB. the solution to this problem could also be employed to solve problem
NB. 76 and 77, but, in practice, this is too slow.

solution =: ways2&(200 100 50 20 10 5 2 1)