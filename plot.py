#!/usr/bin/env python

from matplotlib import pyplot as plt
import random

x = []
y = []
count_of_points = 30
_range = 30000
for i in range(count_of_points):
    x.append(i)

for i in range(count_of_points):
    y.append(random.randint(0, _range))

plt.plot(x, y, label='Received from A')
random.shuffle(y)
plt.plot(x, sorted(y), label='Received from B')

plt.title('RANDOM Data')
plt.xlabel('Dates')
plt.ylabel('Count of files')
plt.legend()
plt.savefig('foo.png', bbox_inches='tight')
