Date: 2025-12-06
Topics: #knn #algorithm 
Link: 
Class: [[]]

---

# KNN or K Nearest Neighbors

This basically predicts the value of a point using the points near it

![KNN Example.png](../../../2_Images/KNN%20Example.png)

We can assume with some certainty that the green point will not own a car since most of the points **near** it (blue) don't own a car

This nearness is calculated by a distance function one of them is **Euclidean Distance**
That is the straight line distance between the green and blue points

The formula is the distance formula learned in high school
assume coordinates of green point is (x1, y1)
assume coordinates of other points is (xN, yN)

distance = sqrt( (x1-xN)^2 + (y1-yN)^2 )

The k in knn refers to how many neighbours we are using to make a prediction about a point
