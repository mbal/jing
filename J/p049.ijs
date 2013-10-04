NB. four digits primes
primes =: p:(168+i.1229-168)

NB. groups anagrams
groups =: ((\:~@":"0) </. ])
NB. is an arithmetic series? Note that a list of number must have a length of
NB. at least 3 to be considered a series.
arith =:((# > 2"_) *. *./@(2 =/\ (}: - }.)) *. (#@~. = #))

NB. I am not very proud of this verb
helper =: 3 : '(3 arith\"1 t) #"(0 0 1) (3 >\"1 t=.(> groups primes))'

NB. solution '' = 0 2969 6299 9629
solution =: ~.@,@helper
