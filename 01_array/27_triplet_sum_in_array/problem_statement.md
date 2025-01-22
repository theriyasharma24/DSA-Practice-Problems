# Problem Statement: [Triplet Sum in Array](https://www.geeksforgeeks.org/problems/triplet-sum-in-array-1587115621/1)

## **Difficulty**: Medium

## Problem Description:

Given an array `arr[]` and an integer `target`, determine if there exists a triplet in the array whose sum equals the given target.

Return `true` if such a triplet exists, otherwise, return `false`.

### Function Signature:

```python
def hasTripletSum(self, arr: List[int], target: int) -> bool:
```

### Input:

- An array `arr[]` of integers.
- An integer `target`, the sum to be checked.

### Output:

- Return `true` if there exists a triplet in the array such that the sum of the triplet is equal to `target`.
- Return `false` otherwise.

---

## Examples:

### Example 1:

**Input**:  
`arr[] = [1, 4, 45, 6, 10, 8]`, `target = 13`

**Output**:  
`true`

**Explanation**:  
The triplet {1, 4, 8} sums up to 13.

---

### Example 2:

**Input**:  
`arr[] = [1, 2, 4, 3, 6, 7]`, `target = 10`

**Output**:  
`true`

**Explanation**:  
The triplets {1, 3, 6} and {1, 2, 7} both sum to 10.

---

### Example 3:

**Input**:  
`arr[] = [40, 20, 10, 3, 6, 7]`, `target = 24`

**Output**:  
`false`

**Explanation**:  
No triplet in the array sums to 24.

---

## Constraints:

- \( 3 \leq \text{arr.size()} \leq 10^3 \)
- \( 1 \leq \text{arr}[i] \leq 10^5 \)
