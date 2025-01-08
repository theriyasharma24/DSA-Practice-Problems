# Problem Statement: [Two Sum - Pairs with 0 Sum](https://www.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1)

## Difficulty: Easy

### Problem Description:

Given an integer array `arr`, return all the unique pairs `[arr[i], arr[j]]` such that `i != j` and `arr[i] + arr[j] == 0`.

- The pairs must be returned in sorted order, the solution array should also be sorted, and the answer must not contain any duplicate pairs.

---

### Input:

- An integer array `arr[]` of size `n`, where:
  - `3 ≤ arr.size ≤ 10^5`
  - `-10^5 ≤ arr[i] ≤ 10^5`

---

### Output:

- A 2D array where each element is a unique pair `[arr[i], arr[j]]` such that `i != j` and `arr[i] + arr[j] == 0`.

---

### Example 1:

**Input:**  
`arr = [-1, 0, 1, 2, -1, -4]`

**Output:**  
`[[-1, 1]]`

**Explanation:**  
`arr[0] + arr[2] = (-1) + 1 = 0`.  
`arr[2] + arr[4] = 1 + (-1) = 0`.  
The distinct pair is `[-1, 1]`.

---

### Example 2:

**Input:**  
`arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]`

**Output:**  
`[[-6, 6], [-1, 1]]`

**Explanation:**  
The distinct pairs are `[-1, 1]` and `[-6, 6]`.

---

### Expected Time Complexity:

- **Time Complexity:** `O(n log n)`  
  (Due to sorting and searching in the array)
- **Auxiliary Space Complexity:** `O(n)`

---

### Constraints:

- `3 ≤ arr.size ≤ 10^5`
- `-10^5 ≤ arr[i] ≤ 10^5`
