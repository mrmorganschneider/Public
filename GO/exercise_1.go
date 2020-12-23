//Loops and Functions excercise from go tour
//https://tour.golang.org/flowcontrol/8

package main

import (
	"fmt"
)

func Sqrt(x float64) float64 {

	z := float64(1)

	//method for 10 iterations
	//for i := 1; i <= 10; i++ {
	//	z = z - (z*z-x)/(2*z)
	//}

	//method for programable iterations
	//change diff for smaller differences

	diff := 0.0000001

	for {
		z = z - (z*z-x)/(2*z)
		fmt.Println(z)
		if (z*z-x)/(2*z) < diff {
			break
		}
	}

	return z
}

func main() {
	fmt.Println(Sqrt(2))
}
