# Lexical scoping assignment

## Assignment description

Matrix inversion is usually a costly computation and there may be some benefit to caching the inverse of a matrix rather than compute it repeatedly (there are also alternatives to matrix inversion that we will not discuss here). Your assignment is to write a pair of functions that cache the inverse of a matrix.

Write the following functions:

makeCacheMatrix: This function creates a special "matrix" object that can cache its inverse.
cacheSolve: This function computes the inverse of the special "matrix" returned by makeCacheMatrix above. If the inverse has already been calculated (and the matrix has not changed), then the cachesolve should retrieve the inverse from the cache.
Computing the inverse of a square matrix can be done with the solve function in R. For example, if X is a square invertible matrix, then solve(X) returns its inverse.

For this assignment, assume that the matrix supplied is always invertible.

## File description

### cachematrix.R

This is the primary submission for the assignment. These two functions calculate the inverse of the matrix supplied and then caches the data in the parent environment. This is done by creating a list that stores both the matrix and its inverse in a parent environment variable. This file only caches one matrix at a time as the list is overwritten every time a new matrix is submitted. 

An extension of this can be found in the cachematrix extended file, which can cache an infinite number of matrices.

#### makeCacheMatrix

This function takes a matrix as input and returns a list which stores the matrix itself and creates a variable for the inverse of the matrix. The function also defines the functions to get and set the matrix and inverse for the list

#### cacheSolve

This function takes a matrix and returns the inverse of said matrix. Note that there is no error checking so you must ensure the matrix provided is invertable. The function also creates a list which caches the matrix and its inverse in the parent environment using the following code:

    matList <<- makeCacheMatrix(x)
    inverseMatrix <- solve(matList$get())
    matList$setInverse(inverseMatrix)

Note that because the list is always stored in the *matList* variable, meaning that every time this function is run for a new matrix, the cached data will be replaced with the new matrix information.

### cachematrix extended.R

This is the secondary submission for the assignment. These two functions calculate the inverse of the matrix supplied and then caches the data in the parent environment. This is done by creating a list that stores both the matrix and its inverse in a parent environment variable. 

The extended version of the assignment can store an infinite number of caches by iterating through each of the existing caches and checking if the data matches the input matrix. If it is not found, the function will create a new cache for the matrix and store the data in the parent environment. 

#### cacheSolve

This function takes a matrix and returns the inverse of said matrix. Note that there is no error checking so you must ensure the matrix provided is invertable. The function also creates a list which caches the matrix and its inverse in the parent environment using the following code:

    matTemp = makeCacheMatrix(x)
    inverseMatrix <- solve(x)
    matTemp$setInverse(inverseMatrix)
    assign(paste("matList", matCount, sep =""), matTemp, pos=1)

Note that because the list is always stored in the *matList* variable, meaning that every time this function is run for a new matrix, the cached data will be replaced with the new matrix information.