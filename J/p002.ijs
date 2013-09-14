fibo =: 3 : 'if. (_1 { y) < 4 * 1e6 do. fibo (y , (_2 { y + _1 { y)) else. y end.'
even =: 0 = 2&|
sol2 =: +/ ((even @ fibo 1 2) # fibo 1 2)
