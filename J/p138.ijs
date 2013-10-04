next =: (8 8) + (_9 _10 ,: _8 _9)&prod
prod =: +/ . *
NB. solution 17 16 = 1118049290473932 (45 microsecs)
solution =: +/@:(|@(0&{"1)@(next^:(<12)))
