# Problem Statement: [Rotate by 90 degree](https://www.geeksforgeeks.org/problems/rotate-by-90-degree0356/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card)

## Difficulty: Medium

### Problem Description:

Given a square matrix `mat[][]`, the task is to rotate it by **90 degrees in a clockwise direction** without using any extra space.

---

### Example 1:

**Input**:

```plaintext
mat = [[1, 2, 3], 
       [4, 5, 6], 
       [7, 8, 9]]
```

**Output**:

```plaintext
7 4 1
8 5 2
9 6 3
```

---

### Example 2:

**Input**:

```plaintext
mat = [[1, 2], 
       [3, 4]]
```

**Output**:

```plaintext
3 1
4 2
```

---

### Example 3:

**Input**:

```plaintext
mat = [[1]]
```

**Output**:

```plaintext
1
```

---

### Constraints:

- `1 ≤ mat.size() ≤ 1000`
- `1 ≤ mat[i][j] ≤ 100`