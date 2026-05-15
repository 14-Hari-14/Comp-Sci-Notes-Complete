Date: 2026-05-14
Topics: #distance_metric #knn #clustering
Purpose:
Link: 
Class: [[]]

---

# Minkowski, Euclidean, and Manhattan Distances

The Minkowski distance is a family of distance metrics parameterized by a positive real number $p$. It generalizes several common distances used in machine learning and data analysis.

## Minkowski distance (general form)

For two points $\mathbf{x},\mathbf{y} \in \mathbb{R}^n$, the Minkowski distance of order $p$ is defined as:

$$
d_p(\mathbf{x},\mathbf{y}) = \left(\sum_{i=1}^n |x_i - y_i|^p\right)^{1/p}
$$

Here $p \ge 1$. The Minkowski distance induces the $L_p$ norm $\|\mathbf{x}-\mathbf{y}\|_p$.

## Manhattan distance ($L_1$)

The Manhattan distance (also called city-block or $L_1$ distance) is the Minkowski distance with $p=1$:

$$
d_1(\mathbf{x},\mathbf{y}) = \sum_{i=1}^n |x_i - y_i|
$$

It measures distance as the sum of absolute coordinate-wise differences.

## Euclidean distance ($L_2$)

The Euclidean distance is the Minkowski distance with $p=2$:

$$
d_2(\mathbf{x},\mathbf{y}) = \left(\sum_{i=1}^n |x_i - y_i|^2\right)^{1/2}
$$

It corresponds to the ordinary straight-line distance in Euclidean space.

## Relationship and usage

- Minkowski with parameter $p$ generalizes both Manhattan ($p=1$) and Euclidean ($p=2$) distances: $d_p$ becomes $d_1$ and $d_2$ for those values respectively.
- Choice of $p$ changes metric sensitivity to large coordinate differences: larger $p$ emphasizes larger individual coordinate differences.
- These distances are commonly used in KNN, clustering, and other algorithms that rely on a notion of similarity between points. DBSCAN and KNN often use Euclidean or Manhattan distances depending on the data and problem.

## Simple idea

- Smaller distance means points are more similar.
- Use $L_1$ for axis-aligned, robust-to-outliers comparisons; use $L_2$ for geometric/Euclidean similarity.

## Used by

- [KNN](../Algorithms/KNN.md)
- [DBSCAN](../Algorithms/DBSCAN.md)