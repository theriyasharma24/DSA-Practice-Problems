Sure! Here's a detailed write-up in the same format as your example, for **Leetcode 876: Middle of the Linked List**:

---

# Problem Statement: [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

## Difficulty: Easy

---

### **Problem Description**

Given the head of a singly linked list, return the **middle node** of the linked list.

If there are two middle nodes, **return the second middle node**.

---

### **Examples**

#### **Example 1**

**Input**:
`head = [1, 2, 3, 4, 5]`

**Output**:
`[3, 4, 5]`

**Explanation**:
The middle node of the list is node `3`. The returned list starts from that node.

---

#### **Example 2**

**Input**:
`head = [1, 2, 3, 4, 5, 6]`

**Output**:
`[4, 5, 6]`

**Explanation**:
The list has two middle nodes `3` and `4`. By the problem’s requirement, we return the second one (`4`).

---

### **Constraints**

* The number of nodes in the list is in the range `[1, 100]`.
* `1 <= Node.val <= 100`
