count =: 3 : 0 M.
    c =. 1
    if. 3 > y do.
        c =. 1
    else.
        c =. 1
        for_a. 3+i.(y-2) do.
            for_b. i.(1+y-a) do.
                c =. c + count (y - (a + b + 1))
            end.
        end.
    end.
    c
)

NB. solution 50 = 14675640049 (31 microsecs)
solution =: count

NB. solution2 50 = 1464560049 (42 microsecs)
solution2 =: +/@:(! (-~ 51"_))@:(2&*@i.@<.&(%&3))
