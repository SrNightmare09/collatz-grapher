import matplotlib as plot

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

        print(num)

# collatz(27)

m = y.copy()
m.sort()

nhn = 100 - (m[-1] % 100) # nhn = nearest hundreds number
ymax = m[-1] + nhn
