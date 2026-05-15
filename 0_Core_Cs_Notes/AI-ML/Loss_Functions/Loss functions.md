Date: 2026-05-14
Topics: #loss_functions #ai #ml
Link: 
Class: [[]]

---

# Loss Functions

This note is a small index of common algorithms and the loss functions or score checks they usually use.

## [[../Algorithms/Linear Regression|Linear Regression]]

- [[MSE]]
- [[MAE]]

## [[../Algorithms/Logistic Regression|Logistic Regression]]

- [[Log Loss]]

## [[../Algorithms/Decision Trees + Random Forest|Decision Trees + Random Forest]]

- [[Gini Impurity]]
- [[Entropy]]

## [[Random Forest]]

- [[Gini Impurity]]
- [[Entropy]]

## [[../Algorithms/XGBoost|XGBoost]]

- [[MSE]] for regression tasks
- [[Log Loss]] for classification tasks

## [[SVM]]

- [[Hinge Loss]]

## [[../Algorithms/KNN|KNN]]

- No direct training loss
- Uses [[Minkowski distance]] to compare points

## [[../Algorithms/Naive Bayes|Naive Bayes]]

- No single common training loss
- Often checked with [[Log Loss]] during evaluation

## [[DBSCAN]]

- No direct loss function
- Uses density rules and Euclidean Distance which is a subsection of [[Minkowski distance]]