fibo =: , (+/@((_1 _2)&{))
helper =: (fibo^:((10&^.)@(_1&{) <: 999"_))^:_

NB. solution 1x 1 = 4782 (0.89 seconds)
solution =: #@helper

fibo2 =: {: , +/
NB. f^:<_ means f^:i.k (with k such that f has a fixpoint).
NB. So it means that the conjuctions keeps all the intermediate results
NB. Using f^:_ would result in the two elements list x y such that x
NB. has 1000 digits, but it wouldn't tell the index of such element
helper2 =: fibo2 ` [ @. (999"_ <: 10&^.@{:) ^: (<_)
NB. solution2 1x 1 = 4782 (0.043 seconds)
solution2 =: >:@#@helper2