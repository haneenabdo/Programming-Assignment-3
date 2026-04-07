import sys

def read_input(filename):
  with open(filename, 'r') as f:
    lines = f.read().splitlines()
  
  K = int(lines[0])
  values = {}
  for i in range(1, K + 1):
    char, val = lines[i].split()
    values[char] = int(val)

  A = lines[K + 1]
  B = lines[K + 2]

  return values, A, B

def lcs(values, A, B):
  n, m = len(A), len(B)

  #dp table
  dp = [[0] * (m + 1) for _ in range(n + 1)]

  #fill DP 
  for i in range(1, n + 1):
    for j in range(1, m + 1):
      if A[i - 1] == B[j - 1]:
        dp[i][j] = dp[i - 1][j - 1] + values[A[i - 1]]
      else:
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

  #reconstruct sequence
  i, j = n, m
  subseq = []

  while i > 0 and j > 0:
    if A[i - 1] == B[j - 1]:
      subseq.append(A[i - 1])
      i -= 1
      j -= 1
    elif dp[i - 1][j] > dp[i][j - 1]:
      i -= 1
    else:
      j -= 1

  subseq.reverse()

  return dp[n][m], ''.join(subseq)

def main():
  if len(sys.argv) < 2:
    print("Usage: python lcs.py <input_file>")
    return
  
  filename = sys.argv[1]

  values, A, B = read_input(filename)
  max_val, subseq = lcs(values, A, B)


  print(max_val)
  print(subseq)

if __name__ == "__main__":
  main()