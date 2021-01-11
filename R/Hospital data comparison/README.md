# Hospital data parsing

## Created by Morgan Schneider

### Overview of assignment

In this assignment, we were provided with the outcome-of-care-measures.csv file and were required to design three functions to extract and parse the data in different ways. The best function was to find the best hospital for a given state and condition provided by the user. We were to search for the conditions "heart attack", "heart failure", and "pneumonia". The rankhospital function was to find the hosptial in a given state that had the given ranking for the condition passed by the user. For example, if a user searched "CA", "heart failure", "8", the function would return the 8th highest ranked hospital for heart failure outcomes. The last function, rankall, was to search the data and find the hospital with the condition and rank provided for each state, i.e if a user searched for "heart attack" and "5", the function would return the hospital in each state that was ranked 5th for heart attack outcomes.

### Function descriptions

#### Commonalities

All of the functions rely on a similar process to read the data from the csv file provided. First, the input data is set to upper or lower case in order to ensure correct matching with the data in the file. From there, a condition checks to ensure a valid outcome has been input by the user. This ensures that no misspelled words are allowed to pass further in the function causing an error. Once the error checking is done, the file is then read for the specific condition in question, reducing the amount of data required to be sorted later in processing.

The reason that I did not put this process into a function is due to the next step. For the rankhosptial and best functions, the user has to input a state that will narrow the search data further. However, the rankall function requires the data for all states in order to function properly. Because this difference would take more time to parameterize than I felt was necessary given the nature of the lesson, I decided not to place the read in a function for simplicity's sake.

Once the input data is read in and the state data extracted if required, a switch statement parses the data further based on the condition input by the user. Once that is complete, hospitals that do not have the required data, represented in the csv by "Not Available", are removed from the data to prevent any issues in reading.

Once this is complete, the values in the condition column are converted to numerics to ensure proper ordering by the order function. Once this is done, the order function is called on the data, first by state, then by condition, and lastly by hospital name. The last of these sorts is to ensure that hospitals with the same values for the outcome of care are in alphabetical order.

The functions differ greatly after these steps and are described in further detail below

#### best.R

This function simply returns the first row of data from the data matrix as all data should be properly sorted at this point. It also checks to see if the following values for the condition outcome for the next hospital are equal and binds them to the output matrix if so. This was a requirement of the assignment.

#### rankhospital.R

After sorting the data as listed in the commonalities section, this function returns the name of the hospital based on the rank of the hospital for the provided condition by the user. For example, if a user searched "CA", "heart failure", "8", the function would return the 8th highest ranked hospital for heart failure outcomes. The function could also return the "best" and "worst" hospitals in the state if these were provided instead of a numeric value.

The first step of this function is to assign a numeric rank to each hospital based on the hospitals location in the data frame. It does so in the following code snippet:

    stateData$Rank <- c(1:nrow(stateData))

The above simply assigns a value from 1 to the number of rows in the data frame to each row of the matrix. 

Once the above is complete, the function simply returns the hospital name where the rank is equal to the user input. If the user input "best", it returns the value with rank = 1 and if the user inputs "worst", it returns the last element of the data frame. 

#### rankall.R

The first step in this function is to rank all of the hospitals in each state for the condition provided by the user. It does so by looping through the data frame and assigning a value for each row incrementing by 1 each time it increments to a new row. If a new state is detected, the counter is reset to 1 and the incrementing begins again.

Once complete, like rankhospital.R, it will then return the name of the hospital in each state with the rank corresponding to the user input. If the user inputs "best", then all of the hospitals with rank 1 are returned. 

If the user inputs "worst", first, a new data frame called hosWorst is created and updated with the appropriate row names. Next, a for loop is created to iterate through the data frame similar to the for loop above. When a new state is detected, the loop finds the name of the hospital in the previous value of the frame and sends the hospital name to an output data frame. This output frame is returned from the function.