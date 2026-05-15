Date: 2025-12-07
Topics: #log_reg #supervised_ml #classification #convexity
Link: 
Class: [[]]

---
Logisitic regression uses linear regression as a base and then sends the output of linear regression through a **SIGMOID function** which squashes the output to a range of 0-1 
It uses the loss function of [[../Loss_Functions/Log Loss|Log Loss]] 
![[../../../2_Images/log_reg_1.jpeg|log_reg_1.jpeg]]

![[../../../2_Images/log_reg_2.jpeg|log_reg_2.jpeg]]

## Convexity
This is a property of a function which is absolutely required to perform gradient descent. The property of convexity states that if you map a function on a graph, and select any 2 random points on the function, then the line joining these 2 points should **NOT** be below the mapping of the function

Why is convexity required
Convexity is required by gradient descent so that it doesnt get stuck at a local minima. Non convex functions will have local minima and once the gradient descent gets stuck at local minima it will never be able to reduce the loss further therefore making non convex loss functions worse than convex functions to train the algorithms. For each a algorithm depending upon its working different loss functions become convex or non convex

![[../../../2_Images/log_reg_convexity_3.jpeg|log_reg_convexity_3.jpeg]]

[[../Gradient Descent|Gradient Descent]] is the most known optimisation routine but in Logistic Regression we dont use Gradient Descent but instead use **LBFGS** 
When we add another matrix known as a Hessian to gradient calculation it becomes Newtons Method to minimise loss
However 2nd derivative matrix is computationally costly to calculate for bigger datasets therefore LBFGS optimises the calculation by storing the change in position and gradient as well as m previous steps to calculate the next direction

![[../../../2_Images/log_reg_lbfgs_4.jpeg|log_reg_lbfgs_4.jpeg]]
