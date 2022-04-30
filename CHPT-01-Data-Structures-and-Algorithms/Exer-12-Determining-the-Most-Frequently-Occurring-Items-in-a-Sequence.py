# 1.12.Determining-the-Most-Frequently-Occurring-Items-in-a-Sequence.py

from collections import Counter

word_counts = Counter(words)

top_three = word_counts.most_common(3)

print(top_three)

print(word_counts['not'])
print(word_counts['eyes'])

morewords = ['why','are','you','not','looking','in','my','eyes']

for word in morewords:
    word_counts[word] +=1

print(word_counts['eyes'])

word_counts.update(morewords)

words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]

morewords = ['why','are','you','not','looking','in','my','eyes']

a = Counter(words)
b = Counter(morewords)

print(a)
print(b)

c = a + b
print(c)

d = a - b
print(d)
