Date: 2026-05-14
Topics: #ensemble_learning #decision_tree #random_forest #supervised_ml #classification #regression 
Link: 
Class: [[]]

---
Decision Tree algorithm can be used for both classification and regression tasks depending upon the implementation.
The basic working of the DT algorithm is it starts at root with yes no questions and splits based on the answers
The splitting stops when some stopping criteria has been met
This algorithm tries to mimic human logical reasoning for example should you go out to play
1. check weather 
2. if weather is good check friends availability
3. if friends are available play
4. if weather bad dont play
5. if friends not available dont play

so similarly DT will split dataset into different trees
There are different algorithms like ID3, CART, SLIQ, etc which use different implementation but the overall idea remains the same

![](DT_1.jpeg)


## Entropy
Defined here: [Entropy](Entropy.md) 
![](DT_Entropy_2.jpeg)


## Gini Impurity
Gini Impurity is better computationally than Entropy because to calculate Impurity we only need to get the square of the probabilities however to get entropy we need to do log<sub>2</sub> calculations which take more time

![](DT_Gini_3.jpeg)

## Decision Trees for Regression
Since numerical data is continuous to split it we use [[MSE]] to calculate which point provides the least error 
We take the midpoints of each feature for each tuple and then check which midpoint provides the least error
![](DT_Bin_Descretization_Regression.jpeg)


## Problems with DT
Decision Trees are low bias and high variance algorithms, that is they can map complex relations decently however they are prone to overfitting to the training data.
This happens because during training
- The tree can become too deep 
- The leaves arent handled properly

To solve this we use **PRUNING**
Types
- Pre-Pruning
- Post-Pruning

![](DT_Pruning_1.jpeg)

## Ensemble Learning
Using a collective of models to solve a problem, its helpful because bringing together multiple low bias high variance models can reduce bias and variance therefore improving the performance
### Bagging
Short for Bootstrapped Aggregation
Bootstrapped -> Randomly sampling with Replacement (this is where the random from Random Forest comes from)
Aggregation -> Combining the output of multiple models to get a better answer (Knowledge of the Crowd)
![](DT_Pruning_bagging.jpeg)

## Bias-Variance Trade-off and Formula for Variance
The trade-off refers to the fact that models with low bias will have high variance and vice versa. Tweaking either will affect the other, the exception of this being ensemble learning techniques.
The formula to calculate variance of a random forest model is 
Variance = $p*\sigma^2 + (1-p*\sigma^2)/n$

$\sigma$ -> variance of 1 tree
p -> correlation between 2 trees
n -> number of trees in the random forest model

Here the first term is the irreducible term that is the minimum amount of overfitting that will be present no matter what 
The other term could be minimized by increasing the number of trees

The major difference between Random Forest and Bagging aside from the fact the RF is a specialised Bagging is that when Random Forest model is being trained **Feature Sampling** for RF is done at each split whereas for bagging its done for each tree therefore RF has less correlation among trees

![](DT_Bagging_RF_bias_variance.jpeg)