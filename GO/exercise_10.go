package main

import (
	"fmt"

	"golang.org/x/tour/tree"
)

// Walk walks the tree t sending all values
// from the tree to the channel ch.

func Walk(t *tree.Tree, ch chan int) {

	leftSum := 0
	rightSum := 0

	if t.Left != nil {
		leftChan := make(chan int)
		go Walk(t.Left, leftChan)
		leftSum = <-leftChan
	}

	if t.Right != nil {
		rightChan := make(chan int)
		go Walk(t.Right, rightChan)
		rightSum = <-rightChan
	}

	total := t.Value + leftSum + rightSum

	ch <- total

}

// Same determines whether the trees
// t1 and t2 contain the same values.
func Same(t1, t2 *tree.Tree) bool {

	returnVal := false

	tree1 := make(chan int)
	tree2 := make(chan int)

	go Walk(t1, tree1)
	go Walk(t2, tree2)

	valTree1 := <-tree1
	valTree2 := <-tree2

	if valTree1 == valTree2 {
		returnVal = true
	}

	return returnVal
}

func main() {

	t1 := tree.New(1)
	t2 := tree.New(2)

	fmt.Println(Same(t1, t2))

}
