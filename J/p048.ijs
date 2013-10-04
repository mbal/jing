NB. last 10 digits of y^y
l1dosp =: (1e10&|@^)~

NB. solution 1000 = 9110846701 (0.039 secs)
solution =: 1e10&|@+/@:l1dosp@i.@>:
