# Problem Statement: [Stock Buy and Sell – Max 2 Transactions Allowed](https://www.geeksforgeeks.org/problems/buy-and-sell-a-share-at-most-twice/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card)

## **Difficulty**: Medium

## **Problem Description**

In daily share trading, a buyer buys shares in the morning and sells them on the same day. If the trader is allowed to make at most 2 transactions in a day, the second transaction can only start after the first one is complete (buy -> sell -> buy -> sell).

The stock prices throughout the day are represented in the form of an array of prices.

Given an array `price` of size `n`, find out the maximum profit that a share trader could have made.

---

## **Examples**

### **Example 1**

**Input**:  
`n = 6`  
`prices[] = {10, 22, 5, 75, 65, 80}`

**Output**:  
`87`

**Explanation**:  
Trader earns 87 as the sum of 12 and 75.

- Buy at 10, sell at 22 (Profit = 12)
- Buy at 5, sell at 80 (Profit = 75)

---

### **Example 2**

**Input**:  
`n = 7`  
`prices[] = {2, 30, 15, 10, 8, 25, 80}`

**Output**:  
`100`

**Explanation**:  
Trader earns 100 as the sum of 28 and 72.

- Buy at 2, sell at 30 (Profit = 28)
- Buy at 8, sell at 80 (Profit = 72)

---

## **Your Task**

You need to complete the function **`maxProfit()`**, which takes:

- An integer array `price`
- Returns the **maximum profit** if only two transactions are allowed.

---

## **Expected Complexity**

- **Time Complexity**: \( O(n) \)
- **Space Complexity**: \( O(n) \)

---

## **Constraints**

- \( 1 \leq n \leq 10^5 \)
- \( 1 \leq \text{price}[i] \leq 10^5 \)
