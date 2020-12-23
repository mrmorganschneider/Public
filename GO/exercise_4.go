package main

import "fmt"

// fibonacci is a function that returns
// a function that returns an int.
func fibonacci() func() int {

	a := 0
	b := 1

	return func() int {
		temp := b
		b = b + a
		a = temp

		return a
	}
}

func mainExercise4() {
	f := fibonacci()
	for i := 0; i < 10; i++ {
		fmt.Println(f())
	}
}
