sumrev =: x:@(+ |.&.":)
palin =: (-: |.)@":

NB. solution 1e4 = 249 (1.05 secs)
solution =: 3 : '+/ -.@palin"0 ((sumrev^:(-.@palin))^:49)"0 (sumrev"0 i.y)'
