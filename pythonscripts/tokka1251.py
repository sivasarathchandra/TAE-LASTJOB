from sys import stdin, stdout

n = stdin.readline().strip().split()
print(n)
q = stdin.readline().strip().split()
print(q)
o1 = {'1': '0', '0': '1'}
o2 = {'1': 'ODD\n', '0': 'EVEN\n'}
for i in range(int(n[1])):
    print(i)
    each = stdin.readline().split()
    print(each)
    pos = int(each[-1]) - 1
    print(pos)
    if each[0] is '1':
        q[pos] = o1[q[pos]]
    else:
        stdout.write(o2[q[pos]])