next =: +/@:*:@:((7$10)&#:)
chain =: (next ^: (-.@e.&(1 89)))^:_
NB. very similar to olegky's solution, and very slow.
NB. solution (1+i.1e7-1)
solution =: [: +/ ((89&=)@chain"0)