
# Problem Statement: [Roman Number to Integer](https://www.geeksforgeeks.org/problems/roman-number-to-integer3201/1)  

## **Difficulty:** Easy  

---

## **Problem Description**  
Given a string `s` in **Roman numeral format**, convert it to an **integer**.  

### **Roman Numeral Values**  
| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

---

## **Examples**  

### **Example 1**  
**Input:**  
```python
s = "IX"
```
**Output:**  
```python
9
```
**Explanation:**  
IX is a Roman numeral where **X (10) - I (1) = 9**.  

---

### **Example 2**  
**Input:**  
```python
s = "XL"
```
**Output:**  
```python
40
```
**Explanation:**  
XL is a Roman numeral where **L (50) - X (10) = 40**.  

---

### **Example 3**  
**Input:**  
```python
s = "MCMIV"
```
**Output:**  
```python
1904
```
**Explanation:**  
- M = 1000  
- CM = **1000 - 100 = 900**  
- IV = **5 - 1 = 4**  
Total = **1000 + 900 + 4 = 1904**  

---

## **Constraints**  
- `1 ≤ |s| ≤ 3999`  
- `s[i] ∈ {I, V, X, L, C, D, M}`  