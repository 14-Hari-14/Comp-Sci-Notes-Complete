Date: 2025-12-12
Topics: #fast_api #streamlit #pydantic
Link: 
Class: [[]]

---

# Backend Notes with python

The backend pipeline in the project has 5 parts to it

1. **SETUP:** Load heavy assets to memory once (fastapi)
2. **REQUEST:** Take user input (streamlit + requests)
3. **VALIDATION:** Validate user input and check if its in the required format (fastapi + pydantic)
4. **SEARCH:** Send data to vector store for search (fastapi + model)
5. **RESPONSE:** Receive data from search and display it in ui (fastapi + streamlit)

The 3 main packages involved in the whole pipeline are

## **[Fastapi](Fastapi.md):** package to create a backend
## **[Pydantic](Pydantic.md):** package to check data and format validity

## **[Uvicorn](Uvicorn.md):** creates a high performance server for python code (ASGI) **Asynchronous Server Gateway Interface** 




