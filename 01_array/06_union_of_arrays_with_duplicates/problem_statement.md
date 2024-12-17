# Problem Statement: [Union of Arrays with Duplicates](https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1)

## Difficulty: Easy

### Problem Description:

You are given two arrays `a[]` and `b[]`. Your task is to determine the total number of distinct elements present in the union of these two arrays. The union of two arrays can be defined as a set containing all distinct elements from both arrays. Repeated occurrences of the same element should be counted only once.

---

### Input:

- Two integer arrays `a[]` and `b[]` of sizes `n` and `m` respectively, where:
  - `1 ≤ a.size(), b.size() ≤ 10^6`
  - `0 ≤ a[i], b[i] ≤ 10^5`

---

### Output:

- An integer representing the total number of distinct elements in the union of the two arrays.

---

### Example 1:

**Input**:  
`a = [1, 2, 3, 4, 5]`  
`b = [1, 2, 3]`

**Output**:  
`5`

**Explanation**:  
The distinct elements in the union of both arrays are `{1, 2, 3, 4, 5}`. The count is `5`.

---

### Example 2:

**Input**:  
`a = [85, 25, 1, 32, 54, 6]`  
`b = [85, 2]`

**Output**:  
`7`

**Explanation**:  
The distinct elements in the union of both arrays are `{85, 25, 1, 32, 54, 6, 2}`. The count is `7`.

---

### Example 3:

**Input**:  
`a = [1, 2, 1, 1, 2]`  
`b = [2, 2, 1, 2, 1]`

**Output**:  
`2`

**Explanation**:  
The distinct elements in the union of both arrays are `{1, 2}`. The count is `2`.

---

### Constraints:

- `1 ≤ a.size(), b.size() ≤ 10^6`
- `0 ≤ a[i], b[i] ≤ 10^5`
