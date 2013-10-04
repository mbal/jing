import itertools

ppprobs = {}
ccprobs = {}

for c in itertools.product(*[range(1, 5)] * 9): 
    ppprobs[sum(c)] = ppprobs.get(sum(c), 0) + 1

for c in itertools.product(*[range(1, 7)] * 6):
    ccprobs[sum(c)] = ccprobs.get(sum(c), 0) + 1

for o in ppprobs:
    ppprobs[o] /= float(4**9)

for o in ccprobs:
    ccprobs[o] /= float(6**6)

prob = 0
for outcome in ppprobs:
    for outcome2 in ccprobs:
        if outcome > outcome2:
            prob += (ppprobs[outcome] * ccprobs[outcome2])
print prob
