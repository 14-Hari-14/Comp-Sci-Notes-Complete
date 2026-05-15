Date: 2026-05-15
Topics: #boosting #ensemble_learning #supervised_ml #classification #regression 
Link: 
Class: [[]]

---
## Boosting
Boosting is the ensemble learning version where the errors of the current tree are fixed by the next tree. This allows a chain of weak learners to become strong

There are 2 types of boosting mainly
1. Adaboost (Adaptive Boosting)
2. Gradient Boosting -> [XGBoost](XGBoost.md) -> LightGBM

The difference between adaboost and gradient boosting is that adaboost tries to improve weights attached to each tuple whereas gradient boosting tries to figure out rules based on how incorrect the tree was.

![[../../../2_Images/Boosting_Types_1.jpeg|Boosting_Types_1.jpeg]]


![[../../../2_Images/Adaboost_1.jpeg|Adaboost_1.jpeg]]


![[../../../2_Images/Gradient_Boosting.jpeg|Gradient_Boosting.jpeg]]

## Gradient Boosting for Classification

To use gradient boosting for classification we need to use a workaround of using the log odds to add the probabilities of each tree since otherwise the probabilities would exceed 1 which is impossible

![[../../../2_Images/Gradient_Boosting_2.jpeg|Gradient_Boosting_2.jpeg]]

The following derivation shows how gradient boosting is actually implmeneted mathematically and how the output is just = $\frac{\sum \text{residuals}}{\sum p(1-p)}$

which can be written as $\frac{\sum \text{gradients}}{\sum \text{hessian}}$

![[../../../2_Images/Gradient_boosting_3.jpeg|Gradient_boosting_3.jpeg]]

![[../../../2_Images/Gradient_boosting_4.jpeg|Gradient_boosting_4.jpeg]]