phi =: */@:<:

NB. quite ugly.
NB. solution 1009 3643 = 399788195976 (1.12 secs)
solution =: 3 : 0
    'p q' =. y
    ph =. phi y
    t =. (#~ (1"_ = (+.&ph))) 2+i.(ph-1)
    t =. (#~ (2"_ = (<: +. (<: p)"_))) t
    t =. (#~ (2"_ = (<: +. (<: q)"_))) t
    +/ t
)

