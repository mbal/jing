f = open('words.txt')
words = []
for line in f:
    words.extend(map(lambda x: x.replace('"', ""), line.split(',')))

f.close()

import itertools

def anagram(w1, w2):
    return sorted(w1) == sorted(w2)

pmax = 0
i = 0
while words:
    anagrams = [words[0]]
    print words[0]
    for j in range(1, len(words)):
        if anagram(words[0], words[j]):
            anagrams.append(words[j])

    numeric = []

    if len(anagrams) == 1:
        i+=1
        words.remove(anagrams[0])
        continue

    L = len(anagrams[0])

    for comb in itertools.permutations(('0','1','2','3','4','5','6','7','8','9'), L):
        prev = comb[0]
        if prev == '0':
            i += 1
            continue
        skip = False
        for c in comb[1:]:
            if c == prev:
                skip = True
                break
            prev = c
        if skip:
            i+=1
            continue


        numbers = anagrams[:]
        for j in range(L):
            letter = anagrams[0][j]
            for k in range(len(numbers)):
                numbers[k] = numbers[k].replace(letter, comb[j])
        n2 = []
        for n in numbers:
            if n[0] == '0':
                skip = True
                break
            else:
                n2.append(int(n))

        if skip:
            continue
        numbers = n2

        for n1 in numbers:
            for n2 in numbers:
                if n1 != n2:
                    sq1 = n1**.5
                    if sq1 == int(sq1):
                        sq2 = n2**.5
                        if sq2 == int(sq2):
                            if max(sq1, sq2) > pmax:
                                pmax = max(sq1, sq2)

    for a in anagrams:
        words.remove(a)
    i += 1

print pmax
