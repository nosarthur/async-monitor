package main

import (
	"fmt"
	"time"
)

var tic = time.Now()

func runAtInterval(dt time.Duration, checker func() bool, stop chan<- struct{}) {
	ticker := time.NewTicker(dt)
	defer ticker.Stop()
	for {
		select {
		case <-ticker.C:
			{
				fmt.Printf("check health %s @%.3s\n", dt, time.Now().Sub(tic))
				bad := checker()
				if bad {
					stop <- struct{}{}
				}
			}
		}
	}
}

func main() {
	ch1 := make(chan struct{})
	ch2 := make(chan struct{})
	ch3 := make(chan struct{})
	allGood := func() bool { return false }
	doomSoon := func() bool { return true }

	go runAtInterval(time.Second*3, allGood, ch1)
	go runAtInterval(time.Second*5, allGood, ch2)
	go runAtInterval(time.Second*16, doomSoon, ch3)

	select {
	case <-ch1:
		fmt.Println("Problem detected on first checker")
	case <-ch2:
		fmt.Println("Problem detected on second checker")
	case <-ch3:
		fmt.Println("Problem detected on third checker")
	}
}
