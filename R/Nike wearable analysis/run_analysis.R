#Nike run analysis program for peer-graded assigment for 
#Getting and cleaning data course project

#Created by Morgan Schneider Jan 27, 2021

library(tidyverse, help, pos = 2, lib.loc = NULL)

#Function to check for data sets and download if not
#present in the current working directory
data_download <- function(URL) {
    download.file(URL, destfile = "nike_data.zip", method = "curl" )
    unzip("nike_data.zip")
}

#check if data has been downloaded and unzipped
if(!file.exists("nike_data.zip")){
    data_download("https://d396qusza40orc.cloudfront.net/getdata%2Fprojectfiles%2FUCI%20HAR%20Dataset.zip")
}

if(!file.exists("UCI HAR Dataset") & file.exists("nike_data.zip")){
    unzip("nike_data.zip")
}

#load data into R
if(file.exists("UCI HAR Dataset")){

    #load activity names
    measurement_names <- (read.table(".\\UCI HAR Dataset\\features.txt", header = FALSE))[,"V2"]

    subject_test <- as_tibble(read.table(".\\UCI HAR Dataset\\test\\subject_test.txt", header = FALSE, sep = " "))
    subject_train <- as_tibble(read.table(".\\UCI HAR Dataset\\train\\subject_train.txt", header = FALSE, sep = " "))

    X_test <- read_fwf(".\\UCI HAR Dataset\\test\\X_test.txt", 
        fwf_empty(".\\UCI HAR Dataset\\test\\X_test.txt", col_names = measurement_names))
    X_train <- read_fwf(".\\UCI HAR Dataset\\train\\X_train.txt", 
        fwf_empty(".\\UCI HAR Dataset\\train\\X_train.txt", col_names = measurement_names))

    Y_test <- as_tibble(read.table(".\\UCI HAR Dataset\\test\\Y_test.txt", header = FALSE, sep = " "))
    Y_train <- as_tibble(read.table(".\\UCI HAR Dataset\\train\\Y_train.txt", header = FALSE, sep = " "))

    names(subject_test) = "Subject"
    names(subject_train) = "Subject"
    names(Y_test) = "Activity"
    names(Y_train) = "Activity"

}else{
    print("ERROR: UCI HAR Dataset doesn't exist")
    quit(save="no")
}

#Merge datasets
test_full <- add_column(subject_test, Y_test, X_test)
train_full <- add_column(subject_train, Y_train, X_train)