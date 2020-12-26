package main

import "fmt"

type IPAddr [4]byte

func (p IPAddr) String() string {
	return fmt.Sprintf("%v.%v.%v.%v", p[1], p[2], p[3], p[4])
}

func mainExercise5() {
	hosts := map[string]IPAddr{
		"loopback":  {127, 0, 0, 1},
		"googleDNS": {8, 8, 8, 8},
	}
	for name, ip := range hosts {
		fmt.Printf("%v: %v\n", name, ip)
	}
}
