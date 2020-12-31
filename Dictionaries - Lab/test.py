import collections

s = "helloworld"
b = collections.Counter(s).most_common(1)
c = collections.Counter(s).most_common(0)


print(b)

print(c)

