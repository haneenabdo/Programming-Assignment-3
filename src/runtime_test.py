import time
from lcs import read_input, lcs

files = [
    "data/test1.in",
    "data/test2.in",
    "data/test3.in",
    "data/test4.in",
    "data/test5.in",
    "data/test6.in",
    "data/test7.in",
    "data/test8.in",
    "data/test9.in",
    "data/test10.in"
]

times = []
sizes = []

for file in files:
    values, A, B = read_input(file)

    start = time.time()
    lcs(values, A, B)
    end = time.time()

    runtime = end - start

    sizes.append(len(A))
    times.append(runtime)

    print(f"{file}: size={len(A)}, time={runtime:.6f}")

# Save results for plotting
with open("data/results.txt", "w") as f:
    for s, t in zip(sizes, times):
        f.write(f"{s} {t}\n")