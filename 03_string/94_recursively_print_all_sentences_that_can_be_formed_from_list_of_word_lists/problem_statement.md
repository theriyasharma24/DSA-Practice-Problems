
# Problem Statement: [Recursively Print All Sentences That Can Be Formed From List of Word Lists](https://www.geeksforgeeks.org/problems/recursively-print-all-sentences-that-can-be-formed-from-list-of-word-lists/1)

## **Difficulty:** Easy  

---

## **Problem Description**  
Given a list of word lists of size `M × N`, the task is to return all possible sentences by selecting one word from each list at a time using **recursion**.

---

## **Example 1**  

### **Input:**  
```
L = {{"you", "we"},
     {"have", "are"}}
```
### **Output:**  
```
{you have}
{you are}
{we have}
{we are}
```
### **Explanation:**  
We form all possible sentences by picking one word from each list while maintaining the order.

---

## **Your Task**  
You **do not** need to read input or print anything.  
Your task is to implement the function **`sentences(L)`**, which takes a **matrix of strings** as input and returns a **list of lists**, where each inner list represents a possible sentence.

---

## **Expected Complexity**  
- **Time Complexity:** `O(MN)`  
- **Auxiliary Space:** `O(MN)`

---

## **Constraints**  
- `1 <= M, N <= 6`  
- `'a' <= sentence[i][j] <= 'z'`
