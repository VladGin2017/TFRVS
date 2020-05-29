N = 65536
lam = int(input("lam: "))
m = int(input("m: "))
u = int(input("u: "))
o = 0
t = 1
x = []
y = []
n = 65527
j = n + 1

for n in range(65527, 65537, 1):
    if n != N:
        while j <= N:
            l = n
            while l <= j - 1:
                if (N - m) <= l <= N:
                    ul = (N - l) * u
                    t *= (ul / (l * lam))
                elif 0 <= l < (N - m):
                    ul = m * u
                    t *= (ul / (l * lam))
                l += 1
                o += (t / (j * lam))
            print(o, n)
            x.append(n)
            y.append(o)
            n += 1
            j += 1
    elif n == N:
        o = (1 / (N * lam))
        print(o, n)
        x.append(n)
        y.insert(0, o)
        n += 1
        j += 1


x.reverse()
f = open('res.txt', 'w')
i = 0
for k in y:
    f.write(str(x[i]) + '  ' + str(k) + '\n')
    i += 1
f.close()
