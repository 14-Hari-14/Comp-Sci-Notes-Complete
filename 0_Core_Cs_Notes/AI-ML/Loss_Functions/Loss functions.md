Date: 2026-05-14
Topics: #loss_functions #ai #ml
Link: 
Class: [[]]

---

# Loss Functions

This note is a small index of common algorithms and the loss functions or score checks they usually use.

## [[Linear Regression]]

- [[MSE]]
- [[MAE]]

## [[Logistic Regression]]

- [[Log Loss]]

## [[Decision Trees + Random Forest]]

- [[Gini Impurity]]
- [[Entropy]]

## [[Random Forest]]

- [[Gini Impurity]]
- [[Entropy]]

## [[XGBoost]]

- [[MSE]] for regression tasks
- [[Log Loss]] for classification tasks

## [[SVM]]

- [[Hinge Loss]]

## [[KNN]]

- No direct training loss
- Uses [[Minkowski distance]] to compare points

## [[Naive Bayes]]

- No single common training loss
- Often checked with [[Log Loss]] during evaluation

## [[DBSCAN]]

- No direct loss function
- Uses density rules and Euclidean Distance which is a subsection of [[Minkowski distance]]