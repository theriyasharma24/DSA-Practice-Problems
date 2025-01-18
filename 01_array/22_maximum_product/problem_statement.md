# Problem Statement: [Maximum Product Subarray](https://www.geeksforgeeks.org/problems/maximum-product-subarray3604/1)

## Difficulty: Medium

### Problem Description:

Given an array `arr[]` containing positive and negative integers (may contain 0 as well), find the maximum product that can be obtained from a subarray of `arr[]`.

---

### Note:

- It is guaranteed that the output fits in a 32-bit integer.

---

### Input:

- An integer array `arr[]` where:
  - \( 1 \leq arr.size() \leq 10^6 \)
  - \( -10 \leq arr[i] \leq 10 \)

---

### Output:

- An integer representing the maximum product of any subarray of `arr[]`.

---

### Examples:

#### **Example 1**:

**Input:**  
`arr = [-2, 6, -3, -10, 0, 2]`

**Output:**  
`180`

**Explanation:**  
The subarray with the maximum product is `{6, -3, -10}` with a product of \( 6 \times (-3) \times (-10) = 180 \).

---

#### **Example 2**:

**Input:**  
`arr = [-1, -3, -10, 0, 6]`

**Output:**  
`30`

**Explanation:**  
The subarray with the maximum product is `{-3, -10}` with a product of \( -3 \times -10 = 30 \).

---

#### **Example 3**:

**Input:**  
`arr = [2, 3, 4]`

**Output:**  
`24`

**Explanation:**  
For an array with all positive elements, the result is the product of all elements: \( 2 \times 3 \times 4 = 24 \).

---

### Constraints:

- \( 1 \leq arr.size() \leq 10^6 \)
- \( -10 \leq arr[i] \leq 10 \)
