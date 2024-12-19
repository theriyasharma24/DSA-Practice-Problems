# Problem Statement: [Kadane's Algorithm](https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1)

## Difficulty: Medium

### Problem Description:

Given an integer array `arr[]`, your task is to find the maximum sum of any contiguous subarray within the array.

---

### Input:

- An integer array `arr[]` of size `n`, where:
  - `1 ≤ arr.size() ≤ 10^5`
  - `-10^9 ≤ arr[i] ≤ 10^4`

---

### Output:

- A single integer representing the maximum sum of any contiguous subarray within the given array.

---

### Example 1:

**Input**:  
`arr = [2, 3, -8, 7, -1, 2, 3]`

**Output**:  
`11`

**Explanation**:  
The subarray `{7, -1, 2, 3}` has the largest sum of `11`.

---

### Example 2:

**Input**:  
`arr = [-2, -4]`

**Output**:  
`-2`

**Explanation**:  
The subarray `{-2}` has the largest sum of `-2`.

---

### Example 3:

**Input**:  
`arr = [5, 4, 1, 7, 8]`

**Output**:  
`25`

**Explanation**:  
The subarray `{5, 4, 1, 7, 8}` has the largest sum of `25`.

---

### Constraints:

- `1 ≤ arr.size() ≤ 10^5`
- `-10^9 ≤ arr[i] ≤ 10^4`
