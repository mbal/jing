load 'files'

data =: _6 <\ ".&.> ((',', 10{a.)&cutopen fread 'triangles.txt')

det =: -/ . *
area =: 3 : '0.5 * | det (|: 3 2 $ y), 1'

area2 =: 3 : '0.5 * | det (|: (2 2 $ y))'
NB. sum3area =: 3 : '(area2 (0 1 2 3 { y)) + (area2 (2 3 4 5 { y)) + area2 (4 5 0 1 { y)'
NB. sums the areas of the three triangles obtained joining two points from the
NB. original triangle and (0, 0). This sum should be equal to the area of the
NB. triangle. If they're different, (0, 0) is outside the triangle.
NB. tacit style is point-less, in this case, since y appears only in last
NB. position, the tacitization is awful, resulting in a lot of [: and @
sum3area =: 3 : '+/ area2"1 ((6 | (2*i.3)+/i.4) {"1 y)'

solution =: +/ (sum3area = area)"1 (>>data)




