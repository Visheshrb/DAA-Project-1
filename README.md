# Experimental vs Theoretical Complexity Analysis

This repository contains a Python program that compares the experimental runtime  with its theoretical time complexity, O((log logn)^2)

## Description

The `sample_function` simulates an algorithm where the outer loop variable and inner loop and from there we calculate time complexity
The program:

- Measures experimental runtimes.
- Calculates the theoretical complexity values.
- Computes a scaling constant by taking the median of the ratio between experimental and theoretical runtimes.
- Plots the experimental runtimes against the scaled theoretical values.
- Outputs a detailed table showing values used and computed metrics.

## How to Run
git clone https://github.com/Visheshrb/DAA-Project-1.git
cd DAA-Project-1
pip install numpy matplotlib pandas
python3 main.py



