load 'common.ijs'

NB. totient(n) can also be computed as 5&p:
totient =: * */@(-. @ % & ~.@q:)
quot =: % totient

NB. example: solution 1e6
solution =: 3 : '2 + n i. >./ n =: quot 2+i.y'
