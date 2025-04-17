# Problem Statement: [Stack using Two Queues](https://www.geeksforgeeks.org/problems/stack-using-two-queues/1)

**Difficulty:** Easy  

---

## **Problem Description**  
Implement a **Stack** using two **queues** `q1` and `q2`.  
You are required to implement two methods:  
- `push(x)`: Inserts element `x` onto the stack.  
- `pop()`: Removes the element on top of the stack and returns it. If the stack is empty, return `-1`.

---

## **Example 1**  
**Input:**  
```
push(2)  
push(3)  
pop()  
push(4)  
pop()  
```

**Output:**  
```
3 4
```

**Explanation:**  
- `push(2)` → stack becomes [2]  
- `push(3)` → stack becomes [2, 3]  
- `pop()` → returns 3, stack becomes [2]  
- `push(4)` → stack becomes [2, 4]  
- `pop()` → returns 4

---

## **Example 2**  
**Input:**  
```
push(2)  
pop()  
pop()  
push(3)
```

**Output:**  
```
2 -1
```

**Explanation:**  
- `push(2)` → stack becomes [2]  
- `pop()` → returns 2  
- `pop()` → returns -1 (stack is empty)  
- `push(3)` → stack becomes [3]

---

## **Your Task:**  
You don't need to read input or print anything.  
You only need to complete the functions:  
- `push(x)`: Push `x` to the stack  
- `pop()`: Pop and return the top element of the stack (or `-1` if empty)

---

## **Expected Time Complexity:**  
- `push(x)`: **O(1)**  
- `pop()`: **O(N)** (where N is the current size of the stack)

## **Expected Auxiliary Space:**  
- **O(N)** (for queue storage)

---

## **Constraints:**  
- `1 <= Number of queries <= 100`  
- `1 <= Size of stack <= 100`  