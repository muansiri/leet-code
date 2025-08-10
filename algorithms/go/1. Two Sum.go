package main

func twoSum(nums []int, target int) []int {
	memoIndex := make(map[int]int)
	for i, v := range nums {
		remain := target - v
		if _, exists := memoIndex[remain]; exists {
			return []int{memoIndex[remain], i}
		}
		memoIndex[v] = i
	}
	return nil
}
