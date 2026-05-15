Date: 2025-12-09
Topics: #project_notes #attention #faiss 
Link: 
Class: [[]]

---
# TOC 

1. Embeddings
2. [[Backend System + Streamlit Notes]]

# Embeddings

We are creating vector embeddings from words that mean capturing the syntactical meaning of text by storing them in vectors.

To simplify the concept of how vector embedding happens, I will reduce the size from 700-800 elements in a vector to 3 to show how they can be visualized in 3D space

## Axioms for vector embedding 
1. Assume that each vector can be converted into an arrow similar to how we learned in physics
2. Vectors pointing to the same direction mean similar things
3. Depending on the size of the sentence / text, the size of the vector changes


Similar vectors would be close by while opposite/unrelated vectors be farther apart
assume we have a vector (1,2,3)

what I have written here is a representation of a vector in its components form that is the final vector would be formed when i draw a point from (0,0,0) to the point that we reach when we go 1 unit in the x axis, 2 units in the y axis and 3 units in the z axis. In the 3D plane we will reach the point (1,2,3) and the line drawn from (0,0,0) to (1,2,3) is the vector that we were referring to earlier

Now one of the other axioms was that similar vectors point in the same direction this is important because this is required for doing **similarity search** on a vector store, the practical applications could be

- [recommendation system]([[Manga Recommendation Project Documentation]])
- to find some sort of underlying pattern, etc

Now to quantify how similar 2 vectors are there 2 methods:
- **Cosine Similarity**
- **Euclidean Distance**

## Cosine Similarity
Using the axiom of similar vectors (with similar meanings) point to the same direction, to find how similar 2 vectors are we calculate the angle between them

0 angle for the same or very similar vectors, passing this through cos function would give us 1
180 angle for opposite or unrelated vectors, passing this through cos function would give us -1


The mathematical representation for cosine function would be 

![[../../2_Images/cosine similarity formula.png|cosine similarity formula.png]]

here the ||u|| or ||v|| refer to the magnitude of the vectors that is how long it is regardless of distance 

## Euclidean Distance similarity

Euclidean distance calculates the distance between the tip of the two vectors, while this doesnt 

To create further notes on the topic read the literature
[Attention Is All You Need](https://arxiv.org/pdf/1706.03762)