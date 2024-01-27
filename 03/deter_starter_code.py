# Recursive computation of the determinant starter code. Tutorial 3 of MATH/CSCI2072 CSI, Ontario Tech U, 2024.
import numpy as np

def deter(A):
# Recursive computation of the determinant. Input: n X n array A. Out: determinant of A (float).
    n =                                                 # Extract number of rows.
    if n==2:                                            # For 2x2 matrix, use definition.
        # First catch the exceptional case n=2.
        
    else:                                               # For larger matrices, compute recursively.
        detA =                                          # Initialize the determinant.
        for i in range(0,n):                            # Cofactor expansion.
            B =                                         # Delete i-th row.
            B =                                         # Delete first column.
            detA +=                                     # Recursive call.
    return detA

