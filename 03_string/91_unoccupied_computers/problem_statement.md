# Problem Statement: [Unoccupied Computers](https://www.geeksforgeeks.org/problems/unoccupied-computers-1646661078/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card)

## **Difficulty:** Easy  
---

## **Problem Description**  
A cafe has **N computers**. Several customers come to the cafe to use these computers. A customer will be **serviced** only if there is any **unoccupied computer** at the moment the customer visits the cafe. If there is **no unoccupied computer**, the customer **leaves the cafe**.  

You are given an **integer** `N` representing the **number of computers** in the cafe and a **sequence of uppercase letters** `S`.  

Each letter in `S` occurs **exactly two times**:
- The **first occurrence** denotes the **arrival** of a customer.
- The **second occurrence** denotes the **departure** of the same customer if they were allocated a computer.  

Your task is to determine the **number of customers who walked away** without using a computer.

---

## **Example 1**  

### **Input:**  
```
N = 3
S = "GACCBDDBAGEE"
```
### **Output:**  
```
1
```
### **Explanation:**  
- Only **customer 'D'** will not be able to get a computer.
- The answer is **1**.

---

## **Example 2**  

### **Input:**  
```
N = 1
S = "ABCBAC"
```
### **Output:**  
```
2
```
### **Explanation:**  
- **Customers 'B' and 'C'** will not be able to get any computers.
- The answer is **2**.

---

## **Your Task**  
You **do not** need to read input or print anything.  
Your task is to implement the function **`solve(N, S)`**, which takes the integer `N` (the number of computers in the cafe) and the string `S` (denoting the arrival and departure of a customer) as input parameters and returns an **integer** representing the **number of customers that walked away** without using a computer.

---

## **Expected Complexity**  
- **Time Complexity:** `O(|S|)`
- **Auxiliary Space:** `O(1)`

---

## **Constraints**  
- `1 <= N <= 26`
- `1 <= |S| <= 52`
- `S` consists of **uppercase English letters**, and **each letter occurs exactly twice**.
