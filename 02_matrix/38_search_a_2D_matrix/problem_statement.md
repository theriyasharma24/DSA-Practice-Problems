# Problem Statement: [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/description/)

## Difficulty: Medium

### Problem Description:

You are given an `m x n` integer matrix `matrix` with the following two properties:

1. Each row is sorted in non-decreasing order.
2. The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` if `target` is in `matrix`, otherwise return `false`.

You must write a solution in **O(log(m \* n))** time complexity.

---

### Example 1:

**Input**:

```plaintext
matrix = [[1,3,5,7],
          [10,11,16,20],
          [23,30,34,60]], target = 3
```

**Output**:

```plaintext
true
```

---

### Example 2:

**Input**:

```plaintext
matrix = [[1,3,5,7],
          [10,11,16,20],
          [23,30,34,60]], target = 13
```

**Output**:

```plaintext
false
```

---

### Constraints:

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-10^4 <= matrix[i][j], target <= 10^4`
