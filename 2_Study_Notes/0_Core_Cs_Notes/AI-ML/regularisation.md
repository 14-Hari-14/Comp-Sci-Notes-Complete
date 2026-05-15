Date: 2026-05-14
Topics: #ml #regularisation #linear_reg 
Purpose:
Link: 
Class: [[]]

---

**Definition:** Regularisation is a technique used in machine learning to prevent overfitting, which otherwise causes models to perform poorly on unseen data. By adding a penalty for complexity, regularisation encourages simpler and more generalisable models.

## Types

#### 1. Lasso Regression

A regression model which uses the L1 regularisation technique is called [LASSO (Least Absolute Shrinkage and Selection Operator)](https://www.geeksforgeeks.org/machine-learning/what-is-lasso-regression/) regression. It adds the absolute value of magnitude of the coefficient as a penalty term to the loss function(L). This penalty can shrink some coefficients to zero which helps in selecting only the important features **(feature selection)** and ignoring the less important ones.

> $\text{Cost} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y_i})^2 + \lambda \sum_{j=1}^{m} |w_j|$

Where

- m: Number of Features
- n: Number of Examples
- $y_i$: Actual Target Value
- $\hat{y}_i$: Predicted Target Value

### 2. Ridge Regression

A regression model that uses the L2 regularisation technique is called [Ridge regression](https://www.geeksforgeeks.org/machine-learning/what-is-ridge-regression/). It adds the squared magnitude of the coefficient as a penalty term to the loss function(L). It handles multicollinearity by shrinking the coefficients of correlated features, reducing their variance and preventing any single feature from dominating the model.

> $\text{Cost} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 + \lambda \sum_{j=1}^{m} w_j^2$

Where,

- n: Number of examples or data points
- m: Number of features i.e predictor variables
- $y_i$​: Actual target value for the i<sup>th</sup> example
- $\hat{y}_i$​​: Predicted target value for the i<sup>th</sup> example
- $w_i$: Coefficients of the features
- λ: Regularisation parameter that controls the strength of regularisation



