path =: 'cipher1.txt'
data =: ',' cutopen (fread path)

NB. similar to ;, but doesn't box the first argument
link =: , <

NB. compute the frequency of each trigram, and then links
NB. to the corresponding trigram (the nub of data)
triFreq =: (~. (_3 <\ data)) link"0 (+/"1 = _3 >\ data)

key =: 1&{"1
maxFreq =: (\: key triFreq) { triFreq 

NB. this will probably correspond to the string 'the'
NB. A similar analysis could be done on single characters, using ' ' (space)
NB. as the most common english character.
the =: > 0 { {. maxFreq

xor =: 22 b.
ckey =: (a. i. 'the') xor (". @ > the)
stringKey =: ckey { a.

text =: (((# data) $ ckey) xor (0".> data)) { a.
