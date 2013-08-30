div =: (1+i.) #~ 0&= @ (|~ (1+i.))
sigma =: +/ @ div

NB. a(n) = (1/n) * Sum_{k=0, 1, ..., n-1} sigma(n-k)*a(k)
NB. M. is the adverb used to memoize. The J's Vocabulary presents
NB. a different formula for the same result in the entry for M.
NB. This is easier, however, but it probably takes a little longer.
H =: 3 : '+/ (sigma @ (y&-) * a)"0 (i.y)' M.
a =: ((% * H) ` 1:) @. (0&=)

solution =: x: a 100