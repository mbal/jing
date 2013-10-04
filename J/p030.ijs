NB. the upper bound is about 355000

f =: +/@([: ^&5 (#:~ (>.@(10&^.) $ 10"_)))

NB. solution (1+i.355000) = 443839 (1 sec)
solution =: +/@(* (= f"0))
