NB. solution 100 = 4075 (0.0029 secs)
NB. I avoided the tacit form since y appears in only one place, therefore
NB. the point free form will be rather ugly.
solution =: 3 : '+/ 1e6 <: , !/~ (1+i.y)'
