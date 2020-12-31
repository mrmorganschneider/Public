## This is an extended version of the assingment that caches an infinite number
## of matricies. Note that there is no error checking so if an error is made,
## you must restart the R terminal to clear the cached data

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

        if(!exists("matCount")){matCount <<- 0}
        
        if(exists("matList1") && !is.null(matList1)){

                for(i in seq_along(1:matCount)){

                        temp <- get(paste("matList",i,sep=""), pos=1)
                        temp$get()

                        if(identical(temp$get(),x)){
                                message("getting cached data")
                                return(temp$getInverse())
                        }
                }
        }

        matCount <<- matCount + 1

        matTemp = makeCacheMatrix(x)
        inverseMatrix <- solve(x)
        matTemp$setInverse(inverseMatrix)
        assign(paste("matList", matCount, sep =""), matTemp, pos=1)

        inverseMatrix
}