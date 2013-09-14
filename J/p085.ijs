NB. this function computes how many smaller rectangle are there in a
NB. rectangle of sides x and y. (x+1 C 2) * (y+1 C 2)
f =: 4 : '(2 ! x+1) * (2 ! y+1)'
table =: f"0/~ i.200

subtable =: | (2*1e6) - table

solution =: */ @ >@mincoord subtable

NB. find the coordinates (x, y) of the minimum
mincoord =: 3 : 0
    min =. (< 0 0) { y
    minx =. 0
    miny =. 0
    for_r. i.#y do.
        for_s. i.(# r { y) do.
            if. (((< r, s) { y) < min) do.
                min =. (< r, s) { y
                minx =. r
                miny =. s
            else.
            end.
        end.
    end.
    < minx, miny
)