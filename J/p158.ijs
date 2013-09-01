NB. To get this formula, I wrote the numbers from 0 to 16 in binary, and then
NB. sieved the invalid.
f =: !&26 * (2&^ - >:)

solution =: x: @: >./ f (1+i.26)