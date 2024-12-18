# Problem Statement: [Rotate an Array by One](https://www.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1)

## Difficulty: Basic

### Problem Description:

Given an array `arr`, rotate the array by one position in a clockwise direction. This means the last element of the array will become the first element, and all other elements will be shifted one position to the right.

---

### Input:

- An integer array `arr` of size `n`, where:
  - `1 ≤ arr.size() ≤ 10^5`
  - `0 ≤ arr[i] ≤ 10^5`

---

### Output:

- The rotated array after shifting all elements one position in a clockwise direction.

---

### Example 1:

**Input**:  
`arr = [1, 2, 3, 4, 5]`

**Output**:  
`[5, 1, 2, 3, 4]`

**Explanation**:  
After rotating the array by one position, `5` comes to the front and the remaining elements are shifted to the right.

---

### Example 2:

**Input**:  
`arr = [9, 8, 7, 6, 4, 2, 1, 3]`

**Output**:  
`[3, 9, 8, 7, 6, 4, 2, 1]`

**Explanation**:  
After rotating the array by one position, `3` comes to the front and the remaining elements are shifted to the right.

---

### Constraints:

- `1 ≤ arr.size() ≤ 10^5`
- `0 ≤ arr[i] ≤ 10^5`
