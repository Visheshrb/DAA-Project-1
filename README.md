# Experimental vs Theoretical Complexity Analysis

This repository contains a Python program that compares the experimental runtime of a sample nested loop function with its theoretically predicted complexity, \( O((\log \log n)^2) \).

## Description

The `sample_function` simulates an algorithm where the outer loop variable `j` grows multiplicatively by 1.2 until it reaches \(\log n\), and the inner loop variable `k` grows by exponentiation to 1.5 until it reaches `n`. The program:

- Measures experimental runtimes (in nanoseconds) over a range of input sizes `n`.
- Calculates the theoretical complexity values based on \((\log \log n)^2\).
- Computes a scaling constant by taking the median of the ratio between experimental and theoretical runtimes.
- Plots the experimental runtimes against the scaled theoretical values on logarithmic scales for visual comparison.
- Outputs a detailed table showing values used and computed metrics.
