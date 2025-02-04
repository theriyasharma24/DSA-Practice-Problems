# Problem Statement: [Median in a row-wise sorted Matrix](https://www.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1)

## Difficulty: Hard

### Problem Description:

Given a row-wise sorted matrix where the number of rows and columns is always **odd**, find the **median** of the matrix.

The **median** is the middle element when all elements are sorted in non-decreasing order.

---

### Example 1:

**Input**:

```plaintext
mat = [[1, 3, 5],
       [2, 6, 9],
       [3, 6, 9]]
```

**Output**:

```plaintext
5
```

**Explanation**: Sorting all elements gives `{1,2,3,3,5,6,6,9,9}`. The median is `5`.

---

### Example 2:

**Input**:

```plaintext
mat = [[1],
       [2],
       [3]]
```

**Output**:

```plaintext
2
```

**Explanation**: Sorting all elements gives `{1,2,3}`. The median is `2`.

---

### Example 3:

**Input**:

```plaintext
mat = [[3],
       [5],
       [8]]
```

**Output**:

```plaintext
5
```

**Explanation**: Sorting all elements gives `{3,5,8}`. The median is `5`.

---

### Constraints:

- `1 <= mat.size(), mat[0].size() <= 400`
- `1 <= mat[i][j] <= 2000`
- The number of rows and columns is always **odd**.
