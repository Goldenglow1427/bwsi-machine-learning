
import numpy as np
from collections import Counter

dists = np.array([[1., 0.1, 3., 2., 10., 1.5, 12.]])
labels = np.array([2,    0,  2,  2,  3,    8,  5]) 
k = 2

count = Counter()

# print(np.argsort(dists))

sorted_labels = np.argsort(dists).reshape(dists.size)
# print(sorted_labels.reshape(sorted_labels.size))

for i in range(k):
    count[int(labels[sorted_labels[i]])] += 1

print(count.most_common())

mx_cnt = 0
ans = 10000

for id, cnt in count.most_common():
    if mx_cnt <= cnt:
        mx_cnt = cnt
        ans = min(ans, id)
    else:
        break


print(ans)