NB. we are looking for fractions of one the following type:
NB. Ax / Bx, xA/xB, Ax/xB or xA/Bx, where x is not 0.
NB. Not all of these are possible, however. The only one is Ax/xB
NB. (since we have that the fractions must be lower than 1).

helper =: 3 : 0
    den =. 1
    num =. 1
    for_a. >:i.9 do.
        for_b. >:i.(<:a) do.
            for_c. >:i.(<:b) do.
                if. ((a + 10*c) * b) = (c*(b + 10*a)) do.
                    den =. den * b
                    num =. num * c
                else.
                end.
            end.
        end.
    end.
    den, num
)

NB. solution '' = 100 (0.9 msec)
solution =: (0&{ % +./) @: helper
