path =: 'base_exp.txt'
data =: _2 ((0&".)&.>)\ (',',10{a.) cutopen (fread path)

lnexps =: * ^.
NB. solution > data = 709 (0.0017 secs)
solution =: >:@(i. >./)@:(lnexps~/"1)
