package main

import "golang.org/x/tour/reader"

type MyReader struct{}

// TODO: Add a Read([]byte) (int, error) method to MyReader.

func (reader MyReader) Read(b []byte) (n int, err error) {

	for i := range b {

		b[i] = 65

	}

	return len(b), nil
}

func mainExercise7() {
	reader.Validate(MyReader{})
}
