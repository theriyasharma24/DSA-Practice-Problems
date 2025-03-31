# Problem Statement: [Minimum Swaps to Sort](https://www.geeksforgeeks.org/problems/minimum-swaps/1)

## Difficulty: Medium  

---

### **Problem Description**  

Given an array `arr[]` of distinct elements, find the minimum number of swaps required to sort the array in strictly increasing order.  

---

### **Examples**  

#### **Example 1**  
**Input**:  
```python
arr = [2, 8, 5, 4]
```
**Output**:  
```python
1
```
**Explanation**:  
Swap `8` with `4` to get the sorted array.

---

#### **Example 2**  
**Input**:  
```python
arr = [10, 19, 6, 3, 5]
```
**Output**:  
```python
2
```
**Explanation**:  
Swap `10` with `3` and `19` with `5` to get the sorted array.

---

#### **Example 3**  
**Input**:  
```python
arr = [1, 3, 4, 5, 6]
```
**Output**:  
```python
0
```
**Explanation**:  
The input array is already sorted.

---

### **Constraints**  
- `1 ≤ arr.size() ≤ 10^5`  
- `1 ≤ arr[i] ≤ 10^9`