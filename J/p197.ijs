f =: 3 : '1e_9 * <. 2^(30.403243784-y^2)'

NB. f@f^:n means (f@f)^:n, (equivalent to f^:2n). If we do f^:_ we
NB. don't reach a fixpoint, since the two components of the array swap
NB. position each iteration (therefore, we need an even number of iteration
NB. to reach the fixpoint).
solution =: 0j9": +/ (f@f^:_) (f _1), _1
