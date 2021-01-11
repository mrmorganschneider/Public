# GO coding examples from the Go language tour page

## Created by Morgan Schneider

### Purpose

This section of my Github Public directory is a space to demonstrate my answers to the coding exercises from the [Go language tour](https://tour.golang.org/list). Each exercise will contain a link to the relevant page from the tour as well as any explanation for non-functionality should the code be downloaded and compiled independently.

A few notes before beginning. First, as Go compiles all files in the same package and requires that only one main function be present, I created the main.go file to contain the main function for all my examples. This file contains the names of the functions to be executed based on the exercise that I am currently working on. You can change this by editing the file in question to change the *main_exercise_name* function in the file to just *main*.

Second, many of these exercises rely on packages present on the Go tour website. While these packages can be downloaded an used to run the functions offline, it is usually quicker and easier just to copy and paste code into the compiler located on the webpage linked rather than deal with the hassle of downloading the packages just for the purpose of these exercises. All exercises that depend on these external packages will be mentioned.

### Examples

#### Exercise 1: Loops and functions <a name="#1-Exercise-1:-Loops-and-functions"></a>

The purpose of this exercise was to create a loop that calculated the value of a square root to a developer-specified value, first using a repeating loop and then to a certain degree of certainty using a method of our choosing. Link to the exercise is [here.](https://tour.golang.org/flowcontrol/8)

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

The purpose of this exercise was to create a process that calculated the value for each element in a slice of slices object. Link to the exercise is [here.](https://tour.golang.org/moretypes/18)

It should be noted that this code will not function independently from the tour website as the exercise requires the importation of the pic package

    import "golang.org/x/tour/pic"

As such, to verify the code works, you must copy the code to the webpage listed above. The resulting image from the code is shown below.

![Excerise 2 output](exercise_2_output.png "Exercise 2 output")

#### Exercise 3: Maps

The objective of this exercise was to create a function that would parse a string and keep count of the number of unique words located in the input. Link to the exercise is [here.](https://tour.golang.org/moretypes/23)

As with exercise 2, the code will not run independently of the website due to the need for the wc package. The function works by first parsing the text using the strings.Fields method and then mapping each word to a unique location in a map, incrementing the value in the map if it already exists or creating a new map entry if not.

#### Exercise 4: Fibonacci closure

The objective of this exercise was to create a function that would calculate the Fibonacci values to a user specified point using a closure. Link to the exercise is [here.](https://tour.golang.org/moretypes/26)

This code will work outside of the website as it does not require any specific packages to function.  

#### Exercise 5: Stringers

The objective of this exercise was to a Stringer function for the IPAddr type that would return the values of an IP address as a string rather than a 4 byte array. Link to the execise is [here.](https://tour.golang.org/methods/18)

This exercise was fairly straightforward as this merely required parsing the input array using the sprintf function as seen below.

	func (p IPAddr) String() string {
		return fmt.Sprintf("%v.%v.%v.%v", p[0], p[1], p[2], p[3])
		}

No major complications encountered in this exercise.

#### Exercise 6: Errors

The objective of this exercise was to implement error handling in case a negative number was introduced into the sqrt function developed in [exercise 1](#1-Exercise-1:-Loops-and-functions). Link to the exercise is [here.](https://tour.golang.org/methods/20)

As a general remark, I have to say that this portion of the tour of Go was really not well explained. I had to dig through a lot of additional references before I was able to get a handle on the error concept. Also, I am aware that this could have been handled using a function call to the previous sqrt function located in exercise 1 when run in an offline environment. However, I wanted to be certain that the code functioned inside the tour website so I implemented the sqrt_2 function in this file.

	func Sqrt_2(x float64) (float64, error) {

#### Exercise 7: Readers

The objective of this exercise was to create a reader interface that replaced all text read by the reader with the character "A".  Link to the exercise is [here.](https://tour.golang.org/methods/22)

I have few comments on this exercise itself as it is fairly straight forward. The only obstacle I faced was again understanding what the exercise wanted as an output. According to the exercise, the desired result was as follows:

> Implement a Reader type that emits an infinite stream of the ASCII character 'A'.

I initially interpreted this direction as creating a reader that printed an infinite number of 'A" characters, which made no sense as a reader function. Further investigation revealed that the exercise wanted what is described in objective.

#### Exercise 8: ROT13Reader

The objective of this exercise was to create a reader that took another reader as input and applied an ROT13 cipher to the characters. Link to the exercise is [here.](https://tour.golang.org/methods/23)

This was one of the more challenging exercises I had encountered to date. My greatest challenge was figuring out how to actually access the value of the first reader that was being read by the rot13reader. I had to perform additional research to find out that the code required an additional de-reference to access the ascii character stored in the initial reader as seen below:

	n, err := z.r.Read(p)

Once I figured that step out, the rest was a fairly trivial job of implementing a switch that checked the character value and made the appropriate change as seen [here](https://en.wikipedia.org/wiki/ROT13).

#### Exercise 9: Image interface

The objective of this exercise was to create the interfaces needed to generate an image similar to the one created in [exercise 2.](#2-Exercise-2:-Slices) Link to the exercise is [here.](https://tour.golang.org/methods/25)

Note that this code will not work apart from the Go tour page as it requires the pic import to function correctly. The results of the code presented are below.

![Exercise 9 output](exercise_9_output.png "Exercise 9 output")

To recreate the image seen in exercise 2, replace 128 in the Image definition with 256.

My biggest challenge with this exercise was implementing the color method. I kept receiving the following errors and was stuck for a while trying to figure out the issue:

	./prog.go:12:29: undefined: color
	./prog.go:14:9: undefined: color
	./prog.go:22:29: undefined: color
	./prog.go:26:9: undefined: color

I initially believed that the color method was imported with the image import. However, after a long time of the above errors, further research lead me to realize that a separate import was required for the color method to be implemented properly.

	import "image"
	import "image/color"

#### Exercise 10: Equivalent Binary Trees

In this exercise, the objective was to implement two functions, Same and Walk, to determine if two binary trees contained the same values using concurrency to recursively path down the trees and compare the results from the channels. Link to the exercise is [here.](https://tour.golang.org/concurrency/7)

Upon further examination, I realized after implementation that my initial implementation of this exercise was not correct. The objective was to check whether or not the values received by the channels created for recursing through the trees received equivalent values, not whether or not the sum of the values of the trees were identical. This result is presented in the exercise 10 corrected file. As I believe that my original work had value in demonstrating the work I had done, I decided to maintain this code here for an example of my work in go.

Goroutines took a while for me to understand the principle of the channel. My initial understanding was that the routines performed the calculations and then returned values once the routine was complete. However, while working on the assignment, it dawned on me that the routines return a continuous stream of data as each value is calculated. This explained why my tests were returning no value but not returning any error as the channels were not closed and data was still being expected. Once I implemented the Closer function to close the channels once the calculations were complete, the results started coming as expected.

#### Exercise 11: Web crawler

In this exercise, the objective was to implement a crawl function using concurrency that crawled through a fake web page listing and returned the web links only if the links had not previously been listed. Link to the exercise is [here.](https://tour.golang.org/concurrency/10)

I admit that this exercise was a challenge for me. The first issue I encountered was that I forgot that a variable could be initialized outside a func, thereby enabling that variable to be accessed by all functions in the package. Initially, I had been trying to implement a func call similar to the [previous exercise](https://tour.golang.org/concurrency/10), which required a major rework of the provided code. Once I realized that this was unusual for these exercises, I performed some research on variable declaration in GO and realized my error. Once the urlStore variable was declared outside my funcs and was accessible by all in the package, this exercise became simpler.

Another major roadblock was realizing that maps can store bool types just like any other types in GO. Initially, I was trying to store the string slice and compare the url in question to the string slice. While this was successful, and in fact similar to the way that the checkVisited method works, once I realized that I could store bool types as the second type in the map, the exercise came together for me.

The last issue I encountered was related to concurrency and waiting. The waitgroup had not been previously discussed in the tour and I was unfamiliar with it's use. While it appeared my solution was working, I could only get the code to print the first output line before the program exited. Only after checking my solution with others did I discover the use of waitgroup to ensure that the main function waits for all goroutines to complete before exiting itself. I believe that the lack of instruction on the use of the waitgroup to ensure goroutines are completed is a serious oversight by the authors of this tutorial.
