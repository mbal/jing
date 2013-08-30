sumd =: 3 : '+/ (10 $~ >: <. 10^.y) #: y'
pow =: (sumd"0@^ = [) * ^

NB. solution = 248155780267521 (0.08 sec)
NB. First we suppose that the result will have 22 digits. (the real solution has
NB. 15 digits, so we've gone a bit too large, but it's not really important).
NB. If the number has 21 digits, the maximum digital sum is 9*n = 9*22 = 198.
NB. So, it means that 198^k = r, where sumd(r) = 198. r is also < 10^21.
NB. (since the result has 22 digits). Solving the equation for K yields:
NB. log(198^k) = log(r) (~= 10^22)
NB. k*log(198) = 22, so k = 22/log(198) = 9.57 = 10.
NB. The maximum exponent is 10.
NB. At this point, we just create a table of numbers that can be written as
NB. x^y with sumd(x^y) = x, with the previously computed restrictions on the
NB. domains of x and y.
solution =: 30 { /:~ ~., (2+x:i.9*22) pow"0/ 2+i.10