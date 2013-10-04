NB. 1e5 is a reasonable upper limit

digits =: #:~ (>.@(10&^.) $ 10"_)
sum_fact =: +/@:!@digits

NB. solution (3+i.1e5) = 40730 (0.3 secs)
solution =: +/@:(* (= sum_fact"0))
