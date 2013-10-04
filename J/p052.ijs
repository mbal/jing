NB. check if all numbers in a list are formed by the same digits
same =: *./@:(*./@:(2&(=/\))"1)@:(/:~&.":"0)

NB. solution 6 = 142857 (0.81 sec)
solution =: 3 : '1e5 + I. same"1 (1e5+i.5e4) */ (1+i.y)'
