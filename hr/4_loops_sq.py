# Task
# The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .

n = int(input())
list = []

for i in range(n):
    if i < n:
        list.append(i)
for i in list:
    print (i*i)
