# Problem Statement: [Arithmetic Number](https://www.geeksforgeeks.org/problems/arithmetic-number2815/1)

## Difficulty: Easy  

---

### **Problem Description**  

Given three integers `a`, `b`, and `c`, determine whether `b` is present in the arithmetic sequence that starts with `a` and has a common difference of `c`. If `b` exists in the sequence, return `True`, otherwise, return `False`.  

---

### **Examples**  

#### **Example 1**  
**Input**:  
```python
a = 1  
b = 2  
c = 4  
```
**Output**:  
```python
False
```
**Explanation**:  
`2` is not present in the arithmetic sequence starting from `1` with a common difference of `4`.  

---

#### **Example 2**  
**Input**:  
```python
a = 2  
b = 10  
c = 2  
```
**Output**:  
```python
True
```
**Explanation**:  
The sequence starting from `2` with a common difference of `2` is:  
`2, 4, 6, 8, 10, ...`  
Since `10` is present in this sequence, the output is `True`.  

---

#### **Example 3**  
**Input**:  
```python
a = 1  
b = 1  
c = 0  
```
**Output**:  
```python
True
```
**Explanation**:  
Since `c = 0`, the sequence consists of only the number `1`, which includes `b = 1`.  

---

### **Constraints**  
- `-10^9 ≤ a, b, c ≤ 10^9`  