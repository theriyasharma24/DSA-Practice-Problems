# Problem Statement: [Minimize the Heights II](https://www.geeksforgeeks.org/problems/minimize-the-heights3351/1)

## Difficulty: Medium

### Problem Description:

Given an array `arr[]` denoting the heights of `N` towers and a positive integer `K`, for each tower, you must perform exactly one of the following operations exactly once:

1. Increase the height of the tower by `K`.
2. Decrease the height of the tower by `K`.

Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

Note:

- It is compulsory to increase or decrease the height by `K` for each tower.
- After the operation, the resultant array should not contain any negative integers.

---

### Input:

- An integer `K` (1 ≤ `K` ≤ 10^7).
- An array `arr[]` of size `N` where:
  - `1 ≤ N ≤ 10^5`
  - `1 ≤ arr[i] ≤ 10^7`

---

### Output:

- The minimum possible difference between the height of the tallest and shortest towers after performing the operations.

---

### Examples:

#### Example 1:

**Input:**  
`k = 2, arr[] = {1, 5, 8, 10}`

**Output:**  
`5`

**Explanation:**  
The array can be modified as `{1+k, 5-k, 8-k, 10-k} = {3, 3, 6, 8}`. The difference between the largest and the smallest is `8-3 = 5`.

#### Example 2:

**Input:**  
`k = 3, arr[] = {3, 9, 12, 16, 20}`

**Output:**  
`11`

**Explanation:**  
The array can be modified as `{3+k, 9+k, 12-k, 16-k, 20-k} = {6, 12, 9, 13, 17}`. The difference between the largest and the smallest is `17-6 = 11`.

---

### Constraints:

- `1 ≤ k ≤ 10^7`
- `1 ≤ n ≤ 10^5`
- `1 ≤ arr[i] ≤ 10^7`
