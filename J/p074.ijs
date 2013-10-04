digitfact =: x:@+/@:(!@"."0@":)

chain =: ((, $: (digitfact@])) ` (#@[)) @.(e.~)

chain2 =: (, (digitfact@{:))^:(-.@({: e. }:))^:_

NB. too slow, but works
solution =: 3 : '+/ 60 = ((0$0) chain"(0 1 0) i.y)'
solution2 =: 3 : '+/ (61 = #@chain2"0 x:i.y)'
