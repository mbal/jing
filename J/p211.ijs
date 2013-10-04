sigma =: [: */ ((<:@(^(2&*@>:))) % (<:@(^ 2:)))/"1 @(__&q:)
sigma2 =: (+ (2&*@])/)/"1 @: (__&q:)
psquare =: x: (i.%:64e6)^2

solution =: [: +/ sigma"0 #~ (psquare e.~ sigma"0)
