# Problem Statement: [Alternate Positive Negative](https://www.geeksforgeeks.org/problems/array-of-alternate-ve-and-ve-nos1401/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card)

## Difficulty: Easy

### Problem Description:

Given an unsorted array `arr` containing both positive and negative numbers, your task is to rearrange the array and convert it into an array of alternate positive and negative numbers without changing the relative order of elements.

---

### Note:

- The resulting array should start with a positive integer (0 will also be considered as a positive integer).
- If any of the positive or negative integers are exhausted, then add the remaining integers in the output array as they are, maintaining their relative order.
- The array may or may not have an equal number of positive and negative integers.

---

### Input:

- An unsorted integer array `arr` where:
  - `1 ≤ arr.size() ≤ 10^6`
  - `-10^6 ≤ arr[i] ≤ 10^6`

---

### Output:

- A rearranged array where positive and negative integers alternate, starting with a positive integer.

---

### Example 1:

**Input:**  
`arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]`

**Output:**  
`[9, -2, 4, -1, 5, -5, 0, -3, 2]`

**Explanation:**  
The positive numbers are `[9, 4, 5, 0, 2]` and the negative numbers are `[-2, -1, -5, -3]`. Alternating them while maintaining relative order gives `[9, -2, 4, -1, 5, -5, 0, -3, 2]`.

---

### Example 2:

**Input:**  
`arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]`

**Output:**  
`[5, -5, 2, -2, 4, -8, 7, 1, 8, 0]`

**Explanation:**  
The positive numbers are `[5, 2, 4, 7, 1, 8, 0]` and the negative numbers are `[-5, -2, -8]`. Alternating them while maintaining relative order gives `[5, -5, 2, -2, 4, -8, 7, 1, 8, 0]`.

---

### Example 3:

**Input:**  
`arr = [9, 5, -2, -1, 5, 0, -5, -3, 2]`

**Output:**  
`[9, -2, 5, -1, 5, -5, 0, -3, 2]`

**Explanation:**  
The positive numbers are `[9, 5, 5, 0, 2]` and the negative numbers are `[-2, -1, -5, -3]`. Alternating them while maintaining relative order gives `[9, -2, 5, -1, 5, -5, 0, -3, 2]`.

---

### Constraints:

- `1 ≤ arr.size() ≤ 10^6`
- `-10^6 ≤ arr[i] ≤ 10^6`
