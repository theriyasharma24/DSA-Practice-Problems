# Problem Statement: [Find Pair Given Difference](https://www.geeksforgeeks.org/problems/find-pair-given-difference1559/1)

## Difficulty: Easy  

---

### **Problem Description**  

Given an array `arr[]` and an integer `x`, return `True` if there exists a **pair of elements** in the array whose **absolute difference** is `x`, otherwise, return `False`.  

---

### **Examples**  

#### **Example 1**  
**Input**:  
```python
arr = [5, 20, 3, 2, 5, 80]
x = 78
```
**Output**:  
```python
True
```
**Explanation**:  
Pair `(2, 80)` has an absolute difference of `78`.

---

#### **Example 2**  
**Input**:  
```python
arr = [90, 70, 20, 80, 50]
x = 45
```
**Output**:  
```python
False
```
**Explanation**:  
There is no pair with an absolute difference of `45`.

---

#### **Example 3**  
**Input**:  
```python
arr = [1]
x = 1
```
**Output**:  
```python
False
```
**Explanation**:  
Since the array contains only one element, no pair exists.

---

### **Constraints**  
- `1 <= arr.size() <= 10^6`  
- `1 <= arr[i] <= 10^6`  
- `0 <= x <= 10^5`  
