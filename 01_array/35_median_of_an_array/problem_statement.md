# Problem Statement: [Median of an array](https://www.geeksforgeeks.org/problems/find-the-median0527/1)

## **Difficulty**: Easy

## Problem Description:

Given an array `arr[]` of integers, your task is to calculate the median.

---

## Examples:

### Example 1:

**Input:**  
`arr[] = [90, 100, 78, 89, 67]`

**Output:**  
`89`

**Explanation:**  
After sorting the array, the elements become `[67, 78, 89, 90, 100]`.  
The middle element is `89`, which is the median.

---

### Example 2:

**Input:**  
`arr[] = [56, 67, 30, 79]`

**Output:**  
`61.5`

**Explanation:**  
After sorting the array, the elements become `[30, 56, 67, 79]`.  
The median is the average of the two middle elements: `(56 + 67) / 2 = 61.5`.

---

### Example 3:

**Input:**  
`arr[] = [1, 2]`

**Output:**  
`1.5`

**Explanation:**  
The array has only two elements: `[1, 2]`.  
The median is the average of these two elements: `(1 + 2) / 2 = 1.5`.

---

## Constraints:

- \(1 \leq \text{arr.size()} \leq 10^5\)
- \(1 \leq \text{arr[i]} \leq 10^5\)
