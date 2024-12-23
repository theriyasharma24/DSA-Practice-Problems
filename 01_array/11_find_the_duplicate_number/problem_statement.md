# Problem Statement: [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)

## Difficulty: Medium

### Problem Description:

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive, there is only one repeated number in `nums`. Return this repeated number.

You must solve the problem without modifying the array `nums` and using only constant extra space.

---

### Input:

- An array `nums` of size `n + 1` where:
  - `1 ≤ n ≤ 10^5`
  - `nums.length == n + 1`
  - `1 ≤ nums[i] ≤ n`
- All integers in `nums` appear only once except for one integer which appears two or more times.

---

### Output:

- An integer representing the duplicate number in the array.

---

### Examples:

#### Example 1:

**Input:**  
`nums = [1, 3, 4, 2, 2]`

**Output:**  
`2`

**Explanation:**  
The number `2` is repeated.

---

#### Example 2:

**Input:**  
`nums = [3, 1, 3, 4, 2]`

**Output:**  
`3`

**Explanation:**  
The number `3` is repeated.

---

#### Example 3:

**Input:**  
`nums = [3, 3, 3, 3, 3]`

**Output:**  
`3`

**Explanation:**  
The number `3` is repeated.

---

### Constraints:

- `1 ≤ n ≤ 10^5`
- `nums.length == n + 1`
- `1 ≤ nums[i] ≤ n`
- All integers in `nums` appear only once except for precisely one integer which appears two or more times.
