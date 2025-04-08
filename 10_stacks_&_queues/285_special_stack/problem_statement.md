
# Problem Statement: [Special Stack](https://www.geeksforgeeks.org/problems/special-stack/1)

**Difficulty:** Easy  

---

### **Problem Description**  
Design a data structure `SpecialStack` that supports all standard stack operations like:  
- `push()`  
- `pop()`  
- `isEmpty()`  
- `isFull()`  

In addition, it must also support:  
- `getMin()` — which returns the **minimum element** from the stack at any time.

---

### **Functionality to Implement**  
You need to complete the following functions:  
- `push(x)`: Push an element `x` onto the stack.  
- `pop()`: Pop the top element from the stack.  
- `isEmpty()`: Returns `True` if the stack is empty, else `False`.  
- `isFull(n)`: Returns `True` if the stack has reached size `n`, else `False`.  
- `getMin()`: Returns the minimum element in the stack.

---

### **Examples**

#### **Example 1**
**Input:**  
```  
Stack: 18 19 29 15 16  
```

**Output:**  
```  
15  
```

**Explanation:**  
The minimum element in the stack is `15`.

---

#### **Example 2**
**Input:**  
```  
Stack: 34 335 1814 86  
```

**Output:**  
```  
34  
```

**Explanation:**  
The minimum element in the stack is `34`.

---

### **Expected Time Complexity:**  
- O(n) (Total time complexity across all operations)  

### **Expected Auxiliary Space:**  
- O(1) (No extra space for minimum tracking beyond stack structure)

---

### **Constraints**
- `1 ≤ stack.size() ≤ 10⁴`
