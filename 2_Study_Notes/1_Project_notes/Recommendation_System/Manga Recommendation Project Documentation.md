Date: 2025-12-09
Topics: #recommendatio_system #ai 
Link: 
Class: [[]]

---

# Project Overview

A content-based recommendation engine for manga/manhwa that generates personalized suggestions using text embeddings and similarity search. It converts each title's metadata (title, description, tags, rating, year) into vector embeddings and retrieves the most similar titles using FAISS. The goal is to build a scalable, explainable recommendation system suitable for real-world deployment.

# Dataset and Other Resources Used

Dataset: https://www.kaggle.com/datasets/victorsoeiro/manga-manhwa-and-manhua-dataset
Google Collab
FAISS
Text embedding model: 

Features Provided in the dataset
- title: Full name of the manga.
- rating: Average rating of the manga by all users in Anime-Planet.
- description: Description of the manga.
- year: Released year of the manga.
- tags: A list of tags for the manga, like Drama, Comedy, or Fantasy.
- cover: The image cover of the manga.

# Preprocessing and Cleaning

Issues fixed inside the dataset

1. Missing descriptions were replaced with a standardized phrase (“**No description available.**”) to maintain consistent input length for embeddings.
2. Converted the years from float to string 2004.0 -> 2004 -> "2004"
3. Missing years and ratings were replaced with standardized phrase ("**Unknown**") 
4. Converted tags from stringified lists to python lists for easier manipulation using **literal_eval**
5. Created another column **combined_text** for each title with all the above features which will be used to create vectors

# System Architecture

![](Anime%20Recommendation%20Project%20Architecture.svg)

# Data Pipeline

1. User enters preferred titles/genres/tags 
2. Search those tags / titles in the database
3. Retrieve the combined_text for those titles
4. Convert combined_text to vector
5. Perform similarity search on all the vector store
6. Get those Ids
7. Fetch the metadata and other information for those covers from db
8. Rank them and show them to the user
9. Maybe show the reasoning behind recommendation


# Technical Notes 

[Manga Recommendation Notes](Manga%20Recommendation%20Notes.md)