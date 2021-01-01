package main

import (
	"image"
	"image/color"

	"golang.org/x/tour/pic"
)

type Image struct {
	w int
	h int
}

func (I Image) ColorModel() color.Model {

	return color.RGBAModel
}

func (I Image) Bounds() image.Rectangle {

	return image.Rect(0, 0, I.w, I.h)
}

func (I Image) At(x, y int) color.Color {

	v := uint8(x * y)

	return color.RGBA{v, v, 255, 255}
}

func mainExercise9() {
	m := Image{512, 512}
	pic.ShowImage(m)
}
