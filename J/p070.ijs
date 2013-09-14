totient =: 5&p:

solution =: 3 : 0
min =. 2
mini =. 2
for_i. 2+i.1e7 do.
    t =. totient i
    if. (\:~ ":i) -: \:~ ":t do.
        if. (i % t) < min do.
            min =. i % t
            mini =. i
        else.
        end.
    else.
    end.
end.
mini
)
