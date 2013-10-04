NB. half a row of pascal's triangle.
pascal_row =: !~ i.@>:@<.@-:

NB. numbers in pascal's triangle that are also square free. C(n, k)
NB. (k ! n in J) is not divisible by a prime greater than n.
square_free =: pascal_row #~ (>:&1)@*./"1@((*:@p:@i.@(p:^:_1)) |"(0 1 0) pascal_row)

NB. solution 51 = 34029210557338 (0.006 secs)
solution =: 3 : '2 + +/~.,square_free"0 (3+i.y-3)'