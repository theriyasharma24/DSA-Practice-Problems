# Problem Statement: [Check If Circular Linked List](https://www.geeksforgeeks.org/problems/circular-linked-list/1)

## Difficulty: Easy

---

### **Problem Description**

Given the `head` of a singly linked list, return **true** if the linked list is **circular**, and **false** otherwise.

A linked list is considered **circular** if it is **not NULL-terminated** and the last node points back to some previous node in the list — typically the head — forming a cycle.

> 🔒 Note: The linked list does **not contain any inner loop** (i.e., only one possible cycle, if present).

---

### **Examples**

#### **Example 1**

**Input**:
A linked list where the last node points back to the head.

**Output**:
`true`

**Explanation**:
The list forms a cycle:
e.g. `1 → 2 → 3 → 4 → 5 → 2 (again)` — This is circular.

---

#### **Example 2**

**Input**:
A linked list ending in `NULL`.

**Output**:
`false`

**Explanation**:
The list does **not** loop back to any previous node, hence it’s not circular.

---

### **Constraints**

* `1 <= number of nodes <= 100`
* `1 <= node.data <= 10^4`
