package main

import (
	"fmt"

	"golang.org/x/tour/tree"
)

// Walk walks the tree t sending all values
// from the tree to the channel ch.

func Closer(t *tree.Tree, ch chan int) {
	Walk(t, ch)
	close(ch)
}

func Walk(t *tree.Tree, ch chan int) {

	if t == nil {
		return
	}

	Walk(t.Left, ch)
	ch <- t.Value
	Walk(t.Right, ch)
}

// Same determines whether the trees
// t1 and t2 contain the same values.
func Same(t1, t2 *tree.Tree) bool {

	returnVal := true
	tree1 := make(chan int)
	tree2 := make(chan int)

	go Closer(t1, tree1)
	go Closer(t2, tree2)

	tree1Val := <-tree1
	tree2Val := <-tree2

	if tree1Val != tree2Val {
		returnVal = false
	}

	return returnVal
}

func main() {

	t1 := tree.New(1)
	t2 := tree.New(1)

	fmt.Println(t1)
	fmt.Println(t2)

	fmt.Println(Same(t1, t2))

}
