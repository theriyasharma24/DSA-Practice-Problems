# Problem Statement: [Count Inversions](https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1)

## Difficulty: Medium

---

### Problem Description:

Given an array of integers `arr[]`, find the **Inversion Count** in the array.  
Two elements `arr[i]` and `arr[j]` form an inversion if:

- `arr[i] > arr[j]` and
- `i < j`.

The **Inversion Count** indicates how far (or close) the array is from being sorted:

- If the array is already sorted, the inversion count is `0`.
- If the array is sorted in reverse order, the inversion count is **maximum**.

---

### Input:

- An integer array `arr[]` of size `n`, where:
  - `1 ≤ arr.length ≤ 10^5`
  - `1 ≤ arr[i] ≤ 10^4`

---

### Output:

- The total **inversion count** in the array.

---

### Examples:

#### Example 1:

**Input**:  
`arr = [2, 4, 1, 3, 5]`

**Output**:  
`3`

**Explanation**:  
The sequence `[2, 4, 1, 3, 5]` has **three inversions**:

- `(2, 1)`
- `(4, 1)`
- `(4, 3)`

---

#### Example 2:

**Input**:  
`arr = [2, 3, 4, 5, 6]`

**Output**:  
`0`

**Explanation**:  
As the sequence is already sorted, there are **no inversions**.

---

#### Example 3:

**Input**:  
`arr = [10, 10, 10]`

**Output**:  
`0`

**Explanation**:  
As all the elements of the array are the same, there are **no inversions**.

---

### Constraints:

- `1 ≤ arr.length ≤ 10^5`
- `1 ≤ arr[i] ≤ 10^4`
