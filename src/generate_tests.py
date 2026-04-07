import random
import string

def random_string(length):
  alphabet = ['a', 'b', 'c', 'd', 'e']
  return ''.join(random.choice(alphabet) for _ in range(length))

def generate_file(filename, length):
  chars = ['a', 'b', 'c', 'd', 'e']

  with open(filename, 'w') as f:
    f.write("5\n")
    for c in chars:
      f.write(f"{c} {random.randint(1,10)}\n")

    A = random_string(length)
    B = random_string(length)

    f.write(A + "\n")
    f.write(B + "\n")

#generate  10 files with increasing size
sizes = [25, 30, 35, 40, 45, 50, 60, 70, 80, 100]

for i, size in enumerate(sizes):
  generate_file(f"data/test{i + 1}.in", size)

print("Test files generated!")