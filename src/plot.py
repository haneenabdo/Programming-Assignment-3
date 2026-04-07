import matplotlib.pyplot as plt

sizes = []
times = []

with open("data/results.txt", "r") as f:
    for line in f:
        s, t = line.split()
        sizes.append(int(s))
        times.append(float(t))

plt.plot(sizes, times, marker='o')
plt.xlabel("Input Size (length of strings)")
plt.ylabel("Runtime (seconds)")
plt.title("LCS Runtime Analysis")
plt.grid()

plt.savefig("data/runtime_plot.png")
plt.show()