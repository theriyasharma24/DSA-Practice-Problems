# Problem Statement: [Merge Without Extra Space](https://www.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card)

## Difficulty: Medium

### Problem Description:

Given two sorted arrays `a[]` and `b[]` of size `n` and `m` respectively, the task is to merge them in sorted order without using any extra space. Modify `a[]` so that it contains the first `n` elements and modify `b[]` so that it contains the last `m` elements.

You must solve the problem without using any extra space.

---

### Input:

- An array `a[]` of size `n`.
- An array `b[]` of size `m`.
- Both arrays are sorted in non-decreasing order.

Constraints:

- `1 <= n, m <= 10^5`
- `0 <= a[i], b[i] <= 10^7`

---

### Output:

- Modify array `a[]` so that it contains the first `n` elements after merging the two arrays.
- Modify array `b[]` so that it contains the last `m` elements after merging the two arrays.
- The merged arrays should be in sorted order.

---

### Examples:

#### Example 1:

**Input:**  
`a[] = [2, 4, 7, 10]`, `b[] = [2, 3]`

**Output:**  
`a[] = [2, 2, 3, 4]`  
`b[] = [7, 10]`

**Explanation:**  
After merging the two sorted arrays, we get `2 2 3 4 7 10`.

---

#### Example 2:

**Input:**  
`a[] = [1, 5, 9, 10, 15, 20]`, `b[] = [2, 3, 8, 13]`

**Output:**  
`a[] = [1, 2, 3, 5, 8, 9]`  
`b[] = [10, 13, 15, 20]`

**Explanation:**  
After merging the two sorted arrays, we get `1 2 3 5 8 9 10 13 15 20`.

---

#### Example 3:

**Input:**  
`a[] = [0, 1]`, `b[] = [2, 3]`

**Output:**  
`a[] = [0, 1]`  
`b[] = [2, 3]`

**Explanation:**  
After merging the two sorted arrays, we get `0 1 2 3`.

---

### Constraints:

- `1 <= a.size(), b.size() <= 10^5`
- `0 <= a[i], b[i] <= 10^7`
