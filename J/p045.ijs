triangle =: 0.5&*@(* >:)
pentagon =: 0.5&*@(* <:@(3&*))
hexagon =: * <:@+:
tripen =: (triangle #~ (triangle e. pentagon))@i.
penhex =: (pentagon #~ (pentagon e. hexagon))@i.
NB. triangle is a subset of hexagon, so, in theory we don't need tripen
tripenhex =: (tripen #~ (tripen e. penhex))
NB. it's quite ugly, but it works
NB. solution 1e5 = 1533776805 (0.124 secs)
solution =: >./@:x:@tripenhex
