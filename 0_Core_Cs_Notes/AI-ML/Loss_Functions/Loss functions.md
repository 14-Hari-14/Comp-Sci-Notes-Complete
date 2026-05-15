Date: 2026-05-14
Topics: #loss_functions #ai #ml
Link: 
Class: [[]]

---

# Loss Functions

This note is a small index of common algorithms and the loss functions or score checks they usually use.

## [Linear Regression](../Algorithms/Linear%20Regression.md)

- [MSE](MSE.md)
- [MAE](MAE.md)

## [Logistic Regression](../Algorithms/Logistic%20Regression.md)

- [Log Loss](Log%20Loss.md)

## [Decision Trees + Random Forest](../Algorithms/Decision%20Trees%20+%20Random%20Forest.md)

- [Gini Impurity](Gini%20Impurity.md)
- [Entropy](Entropy.md)

## [[Random Forest]]

- [Gini Impurity](Gini%20Impurity.md)
- [Entropy](Entropy.md)

## [XGBoost](../Algorithms/XGBoost.md)

- [MSE](MSE.md) for regression tasks
- [Log Loss](Log%20Loss.md) for classification tasks

## [[SVM]]

- [Hinge Loss](Hinge%20Loss.md)

## [KNN](../Algorithms/KNN.md)

- No direct training loss
- Uses [Minkowski distance](Minkowski%20distance.md) to compare points

## [Naive Bayes](../Algorithms/Naive%20Bayes.md)

- No single common training loss
- Often checked with [Log Loss](Log%20Loss.md) during evaluation

## [DBSCAN](../Algorithms/DBSCAN.md)

- No direct loss function
- Uses density rules and Euclidean Distance which is a subsection of [Minkowski distance](Minkowski%20distance.md)