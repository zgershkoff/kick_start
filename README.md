# kick_start
Solutions to Google's Kick Start challenges, and some notes.

## I/O format
This challenge is different from ones I've seen in that instead of expecting you to paste an answer into the web app, or instead of giving you a function name and parameters to access their API, they have lines that are read using `input()` as if the inputs were provided in the command line. Then they listen for printed lines from the code that you provide.

### How to give the output
The input will be several lines consisting of space-separated numbers.
The first line is the number of cases that must be solved in sequence.
The particulars of the following line depend on the problem.
A typical output scheme might look like:

```
num_cases = int(input())

for case in range(num_cases):
    n, k = map(int, input().split(' '))
    # assuming the first line of every case has 2 parameters
    l = map(int, input().split(' '))
    # assuming the 2nd line of every case is a list of integers
    print("Case #{}: {}".format(case+1, solver(l, k)))
    # printing using str.format()
```

As of writing, Google's interpreter does not allow f-strings for Python 3.
