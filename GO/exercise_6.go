package main

import (
	"fmt"
)

type ErrNegativeSqrt float64

func (e ErrNegativeSqrt) Error() string {
	x := float64(e)
	return fmt.Sprintf("Cannot Sqrt negative number: %v", x)
}

func Sqrt_2(x float64) (float64, error) {

	if x < 0 {
		var e = ErrNegativeSqrt(x)
		return 0, e

	} else {

		z := float64(1)
		diff := 0.0000001

		for {
			z = z - (z*z-x)/(2*z)
			fmt.Println(z)
			if (z*z-x)/(2*z) < diff {
				break
			}
		}
		return z, nil
	}
}
func main() {
	fmt.Println(Sqrt_2(2))
	fmt.Println(Sqrt_2(-2))
}
