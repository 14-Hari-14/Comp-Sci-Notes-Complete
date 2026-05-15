Date: 2025-12-05
Topics: #supervised_ml
Link: 
Class: [[]]

---

This is the type of machine learning where a label is provided with the inputs. For example in the data about types of particles captured by a telescope, with all the features a column for class is given which tells if the collection of a specific type of data will make it a gamma particle or hadron particle

Its used to train the model to find the relationship between the data and the output to predict the output for other similar problems

There are two major types of problems in supervised learning

1. **Classification**
2. **Regression**

The core components for this type of learning are

- **Features (X)**: This is the input parameters/data provided to a model
- **Labels (Y)**: This is the output we predict / want to predict 
- **Training Data**: This is the data which will help the model to map the relation between X & Y
- **Model**: Mathematical function that will map X -> Y
- **Loss function**: Measure the accuracy / correctness of a model
- **Optimization Algorithms**: Minimizes the loss function 


### 1. **Classification**

**Goal**: Predict discrete categories/classes
**Examples**:
- Binary: Spam vs. Not spam
- Multi-class: Animal species identification
- Multi-label: Document topic tagging
**Common Algorithms**:
- [Logistic Regression](Algorithms/Logistic%20Regression.md)
- Decision Trees
- Random Forests
- [Support Vector Machines (SVM)](Algorithms/Support%20Vector%20Machines%20(SVM).md)
- Neural Networks
- [KNN](Algorithms/KNN.md)
- [Naive Bayes](Algorithms/Naive%20Bayes.md)


### 2. **Regression**

**Goal**: Predict continuous numerical values
 **Examples**:
- House price prediction
- Stock price forecasting
- Temperature prediction

**Common Algorithms**:
-  [Linear Regression](Algorithms/Linear%20Regression.md)
- Polynomial Regression
- Decision Trees (for regression)
- Gradient Boosting



### Qualitative Features

It refers to categorical data (finite number of categories or groups)

**One Hot Encoding**
If input matches make it 1 else make it zero, its done for **nominal data** where the order of the data doesn't matter for example country or gender, etc

| country | encoding  |
| ------- | --------- |
| Usa     | [1,0,0,0] |
| India   | [0,1,0,0] |
| Canada  | [0,0,1,0] |
| France  | [0,0,0,1] |

**Ordinal data**
Having some sort of inherent order, like a mood rating or age progression
They are the ordered from 1 to n


### Quantitative features
Numerical valued data could be discrete / continuous

