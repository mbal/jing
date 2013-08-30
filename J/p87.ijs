pi =: p:@i.@(p:^:_1)
squ =: (pi (%: 50e6)) ^ 2
cub =: (pi (3 %: 50e6)) ^ 3
for =: (pi (4 %: 50e6)) ^ 4

NB. well, it's not really elegant.
solution =: +/ 50e6 > ~. , squ +/ cub +/ for