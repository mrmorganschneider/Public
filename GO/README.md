# GO coding examples from the Go language tour page

## Created by Morgan Schneider

### Purpose

This section of my Github Public directory is a space to demonstrate my answers to the coding exercises from the [Go language tour](https://tour.golang.org/list). Each exercise will contain a link to the relevant page from the tour as well as any explanation for non-functionality should the code be downloaded and compiled independently.

A note before beginning, as Go compiles all files in the same package and requires that only one main function be present, I created the main.go file to contain the main function for all my examples. This file contains the names of the functions to be executed based on the exercise that I am currently working on. You can change this by editing the file in question to change the *main_exercise_name* function in the file to just *main*

### Examples

#### Exercise 1: Loops and functions

The purpose of this exercise was to create a loop that calculated the value of a square root to a developer-specified value, first using a repeating loop and then to a certain degree of certainty using a method of our choosing. 

The page for this exercise can be found [here.](https://tour.golang.org/flowcontrol/8)

The first method was to use a for loop with 10 iterations to calculate the value of the square root. This can be seen below:

    for i := 1; i <= 10; i++ {
		z = z - (z*z-x)/(2*z)
	}

This line is commented in the file to prevent it from running concurrently with the second method, which uses a defined accuracy value to determine when the difference between the old and new value for the square root is small enough to break the loop.

    diff := 0.0000001

	for {
		z = z - (z*z-x)/(2*z)
		fmt.Println(z)
		if (z*z-x)/(2*z) < diff {
			break
		}
	}

#### Exercise 2: Slices

The purpose of this exercise was to create a process that calculated the value for each element in a slice of slices object. Link to the execise is [here.](https://tour.golang.org/moretypes/18)

It should be noted that this code will not function independently from the tour website as the exercise requies the importation of the pic package

    import "golang.org/x/tour/pic"

As such, to verify the code works, you must copy the code to the webpage listed above. The resulting image from the code is shown below.

![Excerise 2 output](exercise_2_output.png "Exercise 2 output")

#### Exercise 3: Maps

The objective of this exercise was to create a function that would parse a string and keep count of the number of unique words located in the input. Link to the execise is [here.](https://tour.golang.org/moretypes/23)

As with above, the code will not run independently of the website due to the need for the wc package. The function works by first parsing the text using the strings.Fields method and then mapping each word to a unique location in a map, incrementing the value in the map if it already exists or creating a new map entry if not.

#### Exercise 4: Fibonacci closure

The objective of this exercise was to create a function that would calculate the Fibonacci values to a user specified point using a closure. Link to the execise is [here.](https://tour.golang.org/moretypes/26)

This code will work outside of the website as it does not require any specific packages to function.  

#### Exercise 5: Stringers

The objective of this exercise was to a Stringer function for the IPAddr type that would return the values of an IP address as a string rather than a 4 byte array. Link to the execise is [here.](https://tour.golang.org/methods/18)

This exercise was fairly straightforward as this merely required parsing the input array using the sprintf function as seen below.

   func (p IPAddr) String() string {
       return fmt.Sprintf("%v.%v.%v.%v", p[0], p[1], p[2], p[3])
       }

No major complications encountered in this exercise.

#### Exercise 6: Errors

The objective of this exercise was to implement error handling in case a negative number was introduced into the sqrt function developed in exercise 1. Link to the execise is [here.](https://tour.golang.org/methods/20)

As a general remark, I have to say that this portion of the tour of Go was really not well explained. I had to dig through a lot of additional references before I was able to get a handle on the error concept. Also, I am aware that this could have been handled using a function call to the previous sqrt function located in exercise 1 when run in an offile environment. However, I wanted to be certain that the code functioned inside the tour website so I implemented the sqrt_2 function in this file. 

    func Sqrt_2(x float64) (float64, error) {
