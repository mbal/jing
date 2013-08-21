NB. copied from http://www.jsoftware.com/jwiki/Essays/Stirling Numbers
s1=: 1: ` (<:    ((0,]) + [ * ],0:) $:@<:) @. *

NB. numerator =: 3 : '+/ (<.(y+1)%2) {. |. s1 (y+1)'
numerator =: [: +/ <.@(2&(%~)@>:) {. |.@s1@>:

solution =: <.@(!@>: % numerator)