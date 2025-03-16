# Problem Statement: [Min Number of Flips](https://www.geeksforgeeks.org/problems/min-number-of-flips3210/1)

## **Difficulty:** Easy  
---

## **Problem Description**  
Given a **binary string** (containing only `0`s and `1`s), we need to make it a sequence of **alternating characters** by flipping some of the bits. The goal is to **minimize the number of flips** required.

---

## **Example 1**  

### **Input:**  
```
S = "001"
```
### **Output:**  
```
1
```
### **Explanation:**  
We can flip the **0th** bit to `1` to get `"101"`.

---

## **Example 2**  

### **Input:**  
```
S = "0001010111"
```
### **Output:**  
```
2
```
### **Explanation:**  
We can flip the **1st** and **8th** bits to get `"0101010101"`.

---

## **Your Task**  
You **do not** need to read input or print anything.  
Your task is to implement the function **`minFlips(S)`**, which takes the binary string `S` as input and returns the **minimum number of flips required**.

---

## **Expected Complexity**  
- **Time Complexity:** `O(|S|)`
- **Auxiliary Space:** `O(1)`

---

## **Constraints**  
- `1 <= |S| <= 10^5`
- `S` contains only **binary digits (`0` and `1`)**.
