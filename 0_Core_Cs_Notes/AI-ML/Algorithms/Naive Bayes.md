Date: 2025-12-06
Topics: #naive_bayes
Link: 
Class: [[]]

---

# Bayes Theorem of Probability

This theorem describes the probability of event A happening provided that event B already happened

P(A|B) = ( P(B|A) x P (A) ) / P(B)

![[../../../2_Images/naive_bayes.png|naive_bayes.png]]

P(Ck | x<sub>1</sub>, x<sub>2</sub>, ... , x<sub>n</sub>) = P( x<sub>1</sub>, x<sub>2</sub>, ... , x<sub>n</sub> | C<sub>k</sub>) * P(C<sub>k</sub>) / P( x<sub>1</sub>, x<sub>2</sub>, ... , x<sub>n</sub> )

we can say that denominator is constant 
therefore P(Ck | x<sub>1</sub>, x<sub>2</sub>, ... , x<sub>n</sub>) is directly proportional to P( x<sub>1</sub>, x<sub>2</sub>, ... , x<sub>n</sub> | C<sub>k</sub>) * P(C<sub>k</sub>)

The reason this is called naive bayes thm is that we assume all features x<sub>1</sub>, x<sub>2</sub>, ... x<sub>n</sub> are independent of each other that is x<sub>1</sub> has no effect on x<sub>2</sub>, x<sub>3</sub> ... x<sub>n</sub> same for all other features.

therefore
P(Ck | x<sub>1</sub>, x<sub>2</sub>, ... , x<sub>n</sub>) is directly proportional to P(C<sub>k</sub>) <sup>n</sup>∏<sub>i=1</sub> P( x<sub>i</sub> | Ck)

predicted y = argmax( P(C<sub>k</sub>) <sup>n</sup>∏<sub>i=1</sub> P( x<sub>i</sub> | Ck) )
argmax will select the maximum value the expression inside with a valid k value

this is also called **MAP** (Maximum A Posteriori) this will reduce the probability of classification