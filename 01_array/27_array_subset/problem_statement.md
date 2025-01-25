# Problem Statement: [Array Subset](https://www.geeksforgeeks.org/problems/array-subset-of-another-array2317/1)

## **Difficulty**: Basic

## Problem Description:

Given two arrays `a[]` and `b[]` of size `m` and `n` respectively, determine whether `b[]` is a subset of `a[]`. Both arrays are unsorted, and elements are distinct.

---

## Examples:

### Example 1:

**Input**:  
`a[] = [11, 7, 1, 13, 21, 3, 7, 3]`  
`b[] = [11, 3, 7, 1, 7]`

**Output**:  
`true`

**Explanation**:  
All elements of `b[]` are present in `a[]`.

---

### Example 2:

**Input**:  
`a[] = [1, 2, 3, 4, 4, 5, 6]`  
`b[] = [1, 2, 4]`

**Output**:  
`true`

**Explanation**:  
All elements of `b[]` are present in `a[]`.

---

### Example 3:

**Input**:  
`a[] = [10, 5, 2, 23, 19]`  
`b[] = [19, 5, 3]`

**Output**:  
`false`

**Explanation**:  
Element `3` in `b[]` is not present in `a[]`.

---

## Constraints:

- \( 1 \leq a.size(), b.size() \leq 10^5 \)
- \( 1 \leq a[i], b[j] \leq 10^6 \)
