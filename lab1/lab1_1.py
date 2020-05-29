import matplotlib.pyplot as plt

N = 8192
x = []
y = []
m = 1
u = 1

lam = 10 ** (-5)
for n in range(8090, 8200, 10):
    j = 1
    k = 1
    tmr1 = 1
    tmr2 = 1
    summary = 0
    while k <= n - 1:
        while j <= n - 1:
            l = j
            while l <= n - 1:
                if (N - m) <= l <= N:
                    ul = (N - l) * u
                    tmr1 *= (l * lam) * ul
                    #print(tmr1, l)
                    l += 1
                elif 0 <= l < (N - m):
                    ul = u * m
                    tmr1 *= (l * lam) * ul
                    #print(tmr1, l)
                    l += 1
            summary += (1 / (j * lam)) * tmr1
            j += 1
            #print(summary)
            tmr1 = 1
        if (N - m) <= k <= N:
            ul = (N - k) * u
            tmr2 *= (k * lam) * ul
        elif 0 <= k < (N - m):
            ul = m * u
            tmr2 *= (k * lam) * ul
        #print(tmr2)
        k += 1
    T = (tmr2 / u) + summary
    y.append(T)
    x.append(n)
    print(T, n)

f = open('res4.2.txt', 'w')
i = 0
for k in y:
    f.write(str(x[i]) + '   ' + str(k) + '\n')
f.close()


'''
fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(x_1, y_1)
ax.plot(x_2, y_2)
ax.plot(x_3, y_3)
ax.grid()
plt.show()
'''

