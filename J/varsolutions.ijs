NB. solutions to problem that are too small to create a file

prob3 =: >./ q: 600851475143
prob6 =: p:10000

prob15 =: 20 ! 40

NB. prob20 ! 100x = 648
prob20 =: +/@(#:~ (>:@<.@(10&^.) $ 10"_))

prob24 =: (1+1e6) A. '0123456789'
