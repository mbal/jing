sumdig =: +/@("."0@":)
tbl =: ^/~@(>:@x:@i.)

NB. solution 100 = 972 (0.093 secs)
solution =: >./@:(sumdig"0@,@tbl@<:)
