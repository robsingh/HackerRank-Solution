from collections import OrderedDict

words = OrderedDict()

for _ in range(int(raw_input())):
    key = raw_input()
    if key in words:
        words[key] += 1
    else:
        words[key] = 1

print len(Counter(words).keys())    #to count the number of distinct words from the input. 
print ' '.join(map(str, words.values()))
