palin2 =: (-: |.)@#:"0
palin10 =: (-: |.)@":"0

NB. solution 1e6 = 872187 (0.44 secs)
solution =: [: +/ (#~ (palin2 * palin10))@(>:@(2&*)@i.@-:)

NB. solution 1e6 = 872187 (0.219 secs)
solution2 =: 3 : '+/ (#~ palin10) (#~ palin2) (1+2*i.-:y)'
