## This is assignment 2 that calculates the inverse of a matrix and caches the value in 
## a parent environment variable. Note that this function can only cache one value at 
## a time. For a version that can cache infinite matricies, see cachematrix_extended.R

## function to create the list that stores the cached matrix value and data

makeCacheMatrix <- function(x = matrix()) {
        inverseMatrix <- NULL
        set <- function(y) {
                x <<- y
                inverseMatrix <<- NULL
        }
        get <- function() {x}
        setInverse <- function(inverse) { inverseMatrix <<- inverse }
        getInverse <- function() { inverseMatrix }
        list(set = set, get = get,
                setInverse = setInverse,
                getInverse = getInverse)

}


## function to calculate the inverse matrix and store the data in the parent
## environment

cacheSolve <- function(x, ...) {
        ## Return a matrix that is the inverse of 'x'
        
        if(exists("matList") && !is.null(matList)){

                if(identical(matList$get(),x)){
                        message("getting cached data")
                        return(matList$getInverse())
                }
         }

         matList <<- makeCacheMatrix(x)
         inverseMatrix <- solve(matList$get())
         matList$setInverse(inverseMatrix)
         inverseMatrix
}