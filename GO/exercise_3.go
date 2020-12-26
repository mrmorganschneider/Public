package main

import (
	"strings"
	//"golang.org/x/tour/wc"
)

func WordCount(s string) map[string]int {

	inputString := strings.Fields(s)

	var m = make(map[string]int)

	for i := range inputString {

		if m[inputString[i]] == 0 {

			m[inputString[i]] = 1
		} else {

			m[inputString[i]]++
		}
	}

	return m
}

func mainExercise3() {
	wc.Test(WordCount)
}
