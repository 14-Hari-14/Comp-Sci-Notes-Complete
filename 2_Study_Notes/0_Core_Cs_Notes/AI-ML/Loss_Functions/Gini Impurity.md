---
created: 2026-05-14
topics:
  - loss_function
  - gini_impurity
tags:
  - decision_tree
  - loss_function
  - gini_impurity
aliases:
  - Gini Impurity
purpose: To define gini impurity and its usefullness
---

---

# Gini Impurity

Gini Impurity is a measure used by decision trees to check how mixed a group of samples is.

## Simple idea

- A node with only one class has low impurity
- A node with many mixed classes has higher impurity
- The tree tries to split data to reduce impurity

## Used by

- [Decision Trees + Random Forest](../Algorithms/Decision%20Trees%20+%20Random%20Forest.md)
- [[Random Forest]]