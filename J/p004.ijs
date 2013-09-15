is_palin =: (-. |.)@":"0

NB. solution 3 = 906609 (0.52 secs)
solution =: 3 : '>./ (#~ is_palin) ~. , */~ ((10^<:y) + i.(10^y) - 10^<:y)'
