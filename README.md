# Programming-Assignment-3
# Highest Value Longest Common Subseqeunce (HVLCS)

## Student Information
- Name: Haneen Abdo 
- UFID: 6605-6936
- No partner

## Project Description
This project computes the Highest Value Longest Common Subsequence (HVLCS)

The program outputs:
  1. The maximum value of a common subsequence
  2. One subsequence that achieves this value

## How to Run the Program
### Requirements
- Python3 installed 

### Run Command
```bash
python3 src/lcs.py data/example.in
```
### Expected Output
9
cb

## Input Format
The input file must follow this format:
```bash
K
x1 v1
x2 v2
...
xK vK
A
B
```

where:
  - K is the number of characters 
  - Each of the next K lines contain a character and its assigned value
  - A is the first string
  - B is the second string

## Output Format
1. A single integer representing the maximum value
2. One optimal subsequence that achieves this value

## Assumptions
- All characters in strings A and B appear in the value mapping
- Character values non-negative integers
- Input files are properly formatted 
- Strings are non-empty

## Repository Structure
-Programming-Assignment-3
  - src/
    - lcs.py
    - generate_tests.py
    - runtime_test.py
    - plot.py
  - data/
    - example.in
    - example.out
    - test1.in ... test10.in
    - results.txt
    - runtime_plot.png
  - README.md


## Question 1 Answer
To evaluate performance, we generated 10 input files with string lengths ranging from 25 to 100. Each file contains randomly generated strings along with randomly assigned values for each character.

We measured the runtime of the algorithm on each inout and recorded the results. These results were then plotted on a graph.

The graph shows that runtime increases as input size increases. The growth pattern appears to be roughly quadratic, which is consistent with the theoretical time complexity of the algorithm. This makes sense becasue the dp fills an n x m table.

## Question 2 Answer
Let OPT(i,j) represent the maximum value of a common subsequence between the first i characters of string A and the first j characters of string B

Base Cases: 
- OPT(0,j) = 0
- OPT(i,0) = 0

Recurrence: If A[i] == B[j]: OPT(i,j) = OPT(j - 1) + v(A[i])
Otherwise: OPT(i,j) = max(OPT(i - 1, j), OPT(i, j - 1))

Explanation: If the characters match, we include that character and add its value to the optimal solution of the previous subproblem. If they do not match, we take the max val from either excluding the current char of A or B. This ensures we always build the optimal solution from smaller subproblems. 

## Question 3 Answer

Psuedocode:
```python
for i from 0 to n:
  dp[i][0] = 0

for j from 0 to m:
  dp[0][j] = 0

for i from 1 to n:
  for j from 1 to m:
    if A[i] == B[j]:
      dp[i][j] = dp[i - 1][j - 1] + value(A[i])
    else:
      dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
```

Runtime: The algorithm runs in O(nm) time, where n and m are the lengths of the two input strings.

## Reproducibility
To reproduce the results:
1. Clone the repository
2. Run the program using:
```bash
python3 src/lcs.py data/example.in
```
3. Generate test cases:
```bash
python3 src/generate_tests.py
```
4. Run runtime analysis:
```bash
python3 src/runtime_test.py
```
5. Generate the graph:
```bash
python3 src/plot.py
```

All necessary files are included in the repository