package main

import (
	"io"
	"os"
	"strings"
)

type rot13Reader struct {
	r io.Reader
}

func (z *rot13Reader) Read(p []byte) (int, error) {

	n, err := z.r.Read(p)

	for i := range p {
		switch {
		case p[i] >= 65 && p[i] <= 77:
			p[i] = p[i]
		case p[i] >= 97 && p[i] <= 109:
			p[i] = p[i] + 13
		case p[i] >= 78 && p[i] <= 90:
			p[i] = p[i]
		case p[i] >= 110 && p[i] <= 122:
			p[i] = p[i] - 13
		}
	}

	return n, err
}

func main() {
	s := strings.NewReader("Lbh penpxrq gur pbqr!")
	r := rot13Reader{s}
	io.Copy(os.Stdout, &r)
}
