# Problem Statement: Move all negative elements to end

# Problem Link: [Move all negative elements to end](https://www.geeksforgeeks.org/problems/move-all-negative-elements-to-end1813/1)

## Difficulty: Easy

### Problem Description:

You are given an unsorted array `arr[]` containing both negative and positive integers. Your task is to place all negative elements at the end of the array without changing the relative order of positive and negative elements. The operation must be performed in-place.

---

### Input:

- An integer array `arr[]` of size `n` where:
  - `1 ≤ arr.size ≤ 10^6`
  - `-10^9 ≤ arr[i] ≤ 10^9`

---

### Output:

- The array with all negative elements moved to the end while maintaining the relative order of positive and negative elements.

---

### Example 1:

**Input**:  
`arr = [1, -1, 3, 2, -7, -5, 11, 6]`

**Output**:  
`[1, 3, 2, 11, 6, -1, -7, -5]`

**Explanation**:  
By performing the required operations, the positive elements `[1, 3, 2, 11, 6]` are placed first, followed by the negative elements `[-1, -7, -5]`.

---

### Example 2:

**Input**:  
`arr = [-5, 7, -3, -4, 9, 10, -1, 11]`

**Output**:  
`[7, 9, 10, 11, -5, -3, -4, -1]`

**Explanation**:  
The positive elements `[7, 9, 10, 11]` appear first, followed by the negative elements `[-5, -3, -4, -1]`.

---

### Constraints:

- `1 ≤ arr.size ≤ 10^6`
- `-10^9 ≤ arr[i] ≤ 10^9`

---

### Expected Time Complexity: `O(n)`

### Expected Auxiliary Space: `O(n)`
