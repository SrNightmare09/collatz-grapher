import matplotlib.pyplot as plot

# coordinates

x = []
y = []

def collatz(num):

    steps = 0 # count number of steps

    while (num != 1):

        if (num % 2 == 0):
            num /= 2

        else:
            num = 3 * num + 1

        steps += 1

        x.append(steps)
        y.append(int(num))

        # print(num)

collatz(27)

m = y.copy()
m.sort()

nhn = 100 - (m[-1] % 100) # nhn = nearest hundreds number
ymax = m[-1] + nhn

# plotting

plot.title('Collatz Grapher')

plot.xlabel(f'Steps ({x[-1]})')
plot.ylabel(f'Value (Max: {m[-1]})')

plot.xlim(0, x[-1] + 2)
plot.ylim(0, ymax)

plot.plot(x, y)

plot.grid(True)
plot.autoscale(True)

plot.show()
