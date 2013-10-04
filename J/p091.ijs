NB. there are size^2 triangles with right angle in (0, 0).
NB. 3*size^2 triangles have an orizontal and vertical line.
NB. the others are found using the line equation and its normal line.
NB. therefore, the others are min(pointY*gcd(pointY, pointX)/pointX,
NB. (size-pointX)*gcd(..)/pointY)

f =: 4 : '2 * <. (y * fa % x) <. (50-x)*fa % y [ fa =. (x +. y)'

NB. solution '' = 14234 (0.0313 secs)
solution =: 3 : '7500 + +/(, f"(0 0 0)/~ >:i.50)'
