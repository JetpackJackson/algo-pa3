---
title: COP4533 - Programming Assignment 3
author:
- 'Bailey Watkins (UFID: 97706540)'
- 'Patrick McCormack (UFID: 73709580)'
date: 3/28/2026
documentclass: article
geometry: margin=1in
papersize: letter
---

# Readme
## Environment Setup
- Run `make init` if not using `uv`. Otherwise, continue to running the code.

## Running the code
- Run `make run` (python venv) or `make run-uv` (uv) if you wish to manually type the input data (you will be prompted for the proper format.)
- Run `make run assets/<file>` (python venv) or `make run-uv assets/<file>` if you wish to run the code with a provided input file. You may place any input files into the assets folder and run the code using them by providing the file name.

## Compiling the README
- Run `make doc` to use Pandoc and \LaTeX to create a PDF version of the README.

# Written Component

1)
the 10 input files along with the graph is inside the src/assets folder.


2) 

OPT = {

0 // if either string has a length of 0

max( v_i + OPT(i-1, j-1), OPT(i-1, j), OPT(i, j-1) ) //if there is a match: A[i] = B[j] -> v(A[i]) = v(B[j])

max( OPT(i-1, j), OPT(i, j-1) ) // if there's no match: A[i] != B[j]

}

This recurrence equation is correct because:
<br>
a) the base case only needs to consider if either string is empty, which immediately renders the matching and therefore max value to 0
<br>
b) the matching case chooses either the character and its value, or it skips one char or the other, leading to 2 smaller subproblems (max used for taking the best value for optimality)
<br>
c) since there are no matches, the program must skip one char or the other. This leads to 2 subproblems, one for i-1 and the other for j-1. (max used for taking the best value for optimality)
<br>
the use of 'max' gives each subproblem in OPT the max (and therefore best) possible value for the matchings between A and B. 
Building and reusing these optimized subproblems will give the global optimal solution.


3)
