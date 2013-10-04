NB. is pandigital?
pan =: '123456789'"_ -: /:~
NB. multiply x for every element in y and concat
mulcat =: (' '&(-.~))@":@:*

NB. find the pandigital number that can be obtained by y multiplying it for
NB. the range (1, ... 9).
sol =: 3 : '".@> (#~ pan@>) (<@(y&mulcat))\ >:i.8'

NB. a reasonable limit for the search is 1e4, since, if the number were 5
NB. digits long, it wouldn't be possible to get 4 digits with a multiplication
NB. by 2 (therefore it would not count as multiplication)
NB. solution 1e4 = 932718654 (0.36 secs)
solution =: 3 : '>./ (#~ 1&<) (, sol"0 i.y)'
