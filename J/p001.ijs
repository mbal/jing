NB. module of the division by 3 and 5
NB. 1 1           0 0
NB. 2 2           0 0
NB. 0 3   = 0 ==> 1 0 +./" ==>  0 0 1 0 1 1 ... I. ==> gets the indices
NB. 1 4           0 0 (and between the two            of the elements
NB. 2 0           0 1 colums)                          from the N numbers
NB. 0 1           1 0                           +/ sums
NB. ...           ...
NB.
NB. problem 1
sol1 =: 3 : '+/ I. +./"1 (0 = (3 5 (|/"1 0) i.y))'
NB. fuck yeah tacit style
get_mod =: 0 = 3 5 (|/"1 0) i.
or_l =: (+./"1 @: get_mod) # i.
sol1_2 =: +/ @ or_l

