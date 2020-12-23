package main

//import "https://golang.org/x/tour/pic"

func Pic(dx, dy int) [][]uint8 {

	dxSlice := make([][]uint8, dx)

	for i := 0; i < dx; i++ {

		dySlice := make([]uint8, dy)
		for j := 0; j < dy; j++ {

			dySlice[j] = uint8(i * j)
		}

		dxSlice[i] = dySlice
	}

	return dxSlice
}

func mainExercise2() {
	pic.Show(Pic)
}
