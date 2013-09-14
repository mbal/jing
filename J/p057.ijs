NB. Problem 57
NB. It is possible to show that the square root of two can be expressed as an infinite continued fraction.

NB. √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

NB. By expanding this for the first four iterations, we get:
NB. 
NB. 1 + 1/2 = 3/2 = 1.5
NB. 1 + 1/(2 + 1/2) = 7/5 = 1.4
NB. 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
NB. 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
NB. 
NB. The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.
NB. 
NB. In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?

NB. numerator and denominator of a extended number
nd =: 2&x:

NB. ff^:_ == sqrt(2) - 1
ff =: 1x % 2&+

NB. sol i.1000 == 153
sol =: 3 : '+/ >/"1 dn"0 (nd (1+ff^: y 0))'

NB. digit number
dn =: >:@<.@(10&^.)