digits =: 3 : '((>:<.(10^.y)) $ 10)#:y'
bouncy =: -.@((*./ @: (2&(<:/\))) +. (*./ @: (2&(>:/\))))@digits"0

NB. solution 1 0 ( = 1587000 1571130)
solution =: ((>:@(0&{) , {: + bouncy @ >:@{.) ^: (0.99"_ > %~/))^:_
