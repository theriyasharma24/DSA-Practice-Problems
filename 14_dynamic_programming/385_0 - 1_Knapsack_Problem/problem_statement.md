# Problem Statement: [0 - 1 Knapsack Problem](https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1)

**Difficulty:** Medium  

---

## **Problem Description**  
You are given `n` items, each with a specific **weight** and **value**, and a knapsack with a **capacity `W`**.  
The task is to select items such that:

- The **total weight** of selected items ≤ `W`
- The **total value** is maximized

Note:
- You can **either include an item entirely or not at all**.
- **Each item is available only once** (0-1 selection).

---

## **Example 1**  
**Input:**  
```
W = 4  
val[] = [1, 2, 3]  
wt[] = [4, 5, 1]  
```  
**Output:**  
```
3
```  
**Explanation:**  
Pick the last item which has weight 1 and value 3.

---

## **Example 2**  
**Input:**  
```
W = 3  
val[] = [1, 2, 3]  
wt[] = [4, 5, 6]  
```  
**Output:**  
```
0
```  
**Explanation:**  
No item can be picked as all exceed the capacity.

---

## **Example 3**  
**Input:**  
```
W = 5  
val[] = [10, 40, 30, 50]  
wt[] = [5, 4, 2, 3]  
```  
**Output:**  
```
80
```  
**Explanation:**  
Choose item 3 (val=30, wt=2) and item 4 (val=50, wt=3).

---

## **Your Task:**  
You don't need to read input or print anything.  
Implement the function **`knapsack(W, val, wt)`**, which takes:

- `W` → maximum weight of the knapsack  
- `val[]` → values of items  
- `wt[]` → weights of items  

and **returns the maximum value that can be obtained**.

---

## **Expected Time Complexity:**  
- **O(N × W)** where N is the number of items and W is the knapsack capacity.

## **Expected Auxiliary Space:**  
- **O(N × W)** for the dynamic programming table.

---

## **Constraints:**  
- 2 ≤ `val.length` = `wt.length` ≤ 10³  
- 1 ≤ `W` ≤ 10³  
- 1 ≤ `val[i]`, `wt[i]` ≤ 10³