
# Problem Statement: [Majority Element](https://www.geeksforgeeks.org/problems/majority-element-1587115620/1)

**Difficulty:** Medium 
---

### **Problem Description**  
Given an array `arr`. Find the **majority element** in the array.  
If no majority exists, return `-1`.  

A **majority element** in an array is an element that appears **strictly more than** `arr.size() / 2` times in the array.  

---

### **Examples**  

#### **Example 1**  
**Input:**  
```python
arr = [3, 1, 3, 3, 2]
```
**Output:**  
```python
3
```
**Explanation:**  
Since `3` appears more than `n/2` times, it is the majority element.  

---

#### **Example 2**  
**Input:**  
```python
arr = [7]
```
**Output:**  
```python
7
```
**Explanation:**  
Since `7` is the only element and appears more than `n/2` times, it is the majority element.  

---

#### **Example 3**  
**Input:**  
```python
arr = [2, 13]
```
**Output:**  
```python
-1
```
**Explanation:**  
No element appears more than `n/2` times, so there is no majority element.  

---

### **Expected Time Complexity**  
- **O(n)** (Linear time)  

### **Expected Auxiliary Space**  
- **O(1)** (Constant space)  

---

### **Constraints**  
- `1 ≤ arr.size() ≤ 10^5`  
- `0 ≤ arr[i] ≤ 10^5`  
