package main

import (
	"fmt"
)

func main() {
	var r, a float64
	fmt.Scanf("%f", &r)
	a = r * r * 3.14159
	fmt.Printf("A=%.4f\n", a)
}
