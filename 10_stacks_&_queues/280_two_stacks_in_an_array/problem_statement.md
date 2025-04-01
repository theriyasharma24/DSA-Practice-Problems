# Problem Statement: [Two Stacks in an Array](https://www.geeksforgeeks.org/problems/implement-two-stacks-in-an-array/1)

**Difficulty:** Medium  

---

### **Problem Description**  
Your task is to implement **two stacks** using a **single array efficiently**.  
You need to implement **four methods**:  

1. `TwoStacks()`: Initialize the data structures and variables required.  
2. `push1(x)`: Push an element into **Stack 1**.  
3. `push2(x)`: Push an element into **Stack 2**.  
4. `pop1()`: Pop an element from **Stack 1** and return it. If Stack 1 is empty, return `-1`.  
5. `pop2()`: Pop an element from **Stack 2** and return it. If Stack 2 is empty, return `-1`.  

---

### **Examples**  

#### **Example 1**  
**Input:**  
```python
push1(2)
push1(3)
push2(4)
pop1()
pop2()
pop2()
```
**Output:**  
```python
[3, 4, -1]
```
**Explanation:**  
- `push1(2)` → Stack1 = `{2}`  
- `push1(3)` → Stack1 = `{2, 3}`  
- `push2(4)` → Stack2 = `{4}`  
- `pop1()` → Pops `3` from Stack1 → Stack1 = `{2}`  
- `pop2()` → Pops `4` from Stack2 → Stack2 = `{}`  
- `pop2()` → Stack2 is empty, returns `-1`  

---

#### **Example 2**  
**Input:**  
```python
push1(1)
push2(2)
pop1()
push1(3)
pop1()
pop1()
```
**Output:**  
```python
[1, 3, -1]
```
**Explanation:**  
- `push1(1)` → Stack1 = `{1}`  
- `push2(2)` → Stack2 = `{2}`  
- `pop1()` → Pops `1` from Stack1 → Stack1 = `{}`  
- `push1(3)` → Stack1 = `{3}`  
- `pop1()` → Pops `3` from Stack1 → Stack1 = `{}`  
- `pop1()` → Stack1 is empty, returns `-1`  

---

#### **Example 3**  
**Input:**  
```python
push1(2)
push1(3)
push1(4)
pop2()
pop2()
pop2()
```
**Output:**  
```python
[-1, -1, -1]
```
**Explanation:**  
- `push1(2)` → Stack1 = `{2}`  
- `push1(3)` → Stack1 = `{2, 3}`  
- `push1(4)` → Stack1 = `{2, 3, 4}`  
- `pop2()` → Stack2 is empty, returns `-1`  
- `pop2()` → Stack2 is empty, returns `-1`  
- `pop2()` → Stack2 is empty, returns `-1`  

---

### **Expected Time Complexity**  
- **O(1)** (Constant time) per operation  

### **Expected Auxiliary Space**  
- **O(1)** (No extra space beyond the given array)  

---

### **Constraints**  
- `1 ≤ number of queries ≤ 10⁴`  
- `1 ≤ number of elements in the stack ≤ 100`  
- The sum of the count of elements in both stacks is **less than** the size of the given array.  