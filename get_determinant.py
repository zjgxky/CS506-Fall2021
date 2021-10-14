#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 11:35:31 2021

@author: xukaiyan
"""

def copy_matrix(A):
    col_num = len(A)
    line_num = len(A[0])
    A_copy = []
    for i in A:
        col = []
        for j in i:
            col.append(j)
        A_copy.append(col)
    return A_copy

def get_determinant(A):
    """
    Find determinant of a square matrix using full recursion
        :param A: the matrix to find the determinant for
        :param total=0: safely establish a total at each recursion level
        :returns: the running total for the levels of recursion
    """
    
    indices = list(range(len(A)))
    print(indices)
    

    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val
    
    total = 0

    
    for index in range(len(A)):  
        A_copy = copy_matrix(A)  
        A_copy = A_copy[1:]  
        height = len(A_copy)

        for i in range(height):  
            A_copy[i] = A_copy[i][0:index] + A_copy[i][index+1:]  

        sign = (-1) ** (index % 2)  
        sub_deter = get_determinant(A_copy)  #
        total += sign * A[0][index] * sub_deter  

    return total

A = [[1,5,1],[2,6,7],[2,1,1]]
B = [[1,5],[6,2]]
print(get_determinant(A))
print(get_determinant(B))
