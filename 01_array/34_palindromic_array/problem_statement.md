## Problem Statement: [Palindromic Array](https://www.geeksforgeeks.org/problems/palindromic-array-1587115620/1)

## **Difficulty**: Basic

## Problem Description:

Given an array `arr[]` of positive integers, return `true` if all the elements in the array are palindromes. Otherwise, return `false`.

---

## Examples:

### Example 1:

**Input:**  
`arr = [111, 222, 333, 444, 555]`

**Output:**  
`true`

**Explanation:**

- `111` is a palindrome.
- `222` is a palindrome.
- `333` is a palindrome.
- `444` is a palindrome.
- `555` is a palindrome.

Since all numbers are palindromes, the function returns `true`.

---

### Example 2:

**Input:**  
`arr = [121, 131, 20]`

**Output:**  
`false`

**Explanation:**

- `121` is a palindrome.
- `131` is a palindrome.
- `20` is **not** a palindrome.

Since `20` is not a palindrome, the function returns `false`.

---

## Expected Complexity:

- **Time Complexity**: \(O(n \log n)\)
- **Space Complexity**: \(O(1)\)

---

## Constraints:

- \(1 \leq arr.size() \leq 20\)
- \(1 \leq arr[i] \leq 10^5\)
