# Problem Statement: Sort 0s, 1s, and 2s

# Problem Link: [Sort an Array of 0s, 1s, and 2s](https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1)

## Difficulty: Easy

### Problem Description:

You are given an array `arr[]` containing only 0s, 1s, and 2s. Your task is to sort the array in ascending order.

The array may contain the elements in any random order, but you need to arrange the elements such that all 0s come first, followed by all 1s, and then all 2s. The sorting should be done in-place, with a time complexity of O(n) and O(1) auxiliary space.

### Input:

- An array `arr[]` of size `n` (1 ≤ n ≤ 10^6), where each element is one of {0, 1, 2}.

### Output:

- Return the sorted array in ascending order, with all 0s first, followed by 1s, and then 2s.

### Example 1:

**Input**:  
`arr = [0, 1, 2, 0, 1, 2]`

**Output**:  
`[0, 0, 1, 1, 2, 2]`

**Explanation**:  
The elements of the array are 0, 1, 2, 0, 1, 2. After sorting, the array becomes `[0, 0, 1, 1, 2, 2]`.

---

### Example 2:

**Input**:  
`arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]`

**Output**:  
`[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]`

**Explanation**:  
The elements of the array are 0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1. After sorting, the array becomes `[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]`.

---

### Constraints:

- `1 <= arr.size() <= 10^6`
- `0 <= arr[i] <= 2`
