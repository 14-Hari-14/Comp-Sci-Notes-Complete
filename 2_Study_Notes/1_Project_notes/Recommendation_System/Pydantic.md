Date: 2025-12-12
Topics: #pydantic 
Purpose:
Link: 
Class: [[]]

---

## **Pydantic**

Before writing any server logic we should define the schema for the requests that will be going to and fro from the server this is achieved with pydantic.

Its a python module mainly used to check the validity and settings management 
The requests that are passed to and from the server needs to have a consistent format, the server needs to know 
1. what kind of data is expected (**name** of the field)
2. what is the **type** of that data 

without pydantic we would have to write a lot of if else statements, this problem is solved by pydantic by allowing us to define a schema using the **BaseModel** class 

the following example shows how its used in this project

```python
from pydantic import BaseModel, Field

# Defines the expected JSON structure from the Streamlit frontend
class RecommendationRequest(BaseModel):
    query: str = Field(..., description="User's natural language search query.")
    genres: list[str] = Field(default_factory=list)
    themes: list[str] = Field(default_factory=list)
    demographics: list[str] = Field(default_factory=list)
    # The 'k' value (number of results) can also be sent
    k: int = 5
```

**class RecommendationRequest(BaseModel)**
- describing the `basemodel` class to define schema

**query: str = Field(..., description="users natural language search query)** 
- the lhs describes what data is going to be received right now which is the query field and the type should be str
- the rhs describes other metadata of the input 
	- **...** -> signifies that the field is necessary
	- **description** -> used to generate api documentation by fastapi

**genres: list[str] = Field(default_factory=list)**
- the lhs again describes what data and the type of data provided to the server
- When you set a default value like `list()` or `dict()` in a Pydantic model (or any Python class), Python creates **ONE shared object** for ALL instances. This means if Instance 1 adds something to its list, Instance 2 automatically has it too! This causes weird bugs where data "leaks" between different requests/objects.
- `default_factory=list` tells Pydantic: "When creating a new instance, call `list()` to make a FRESH empty list for this specific instance." Every object gets its own independent list.

**QUICK RULE:**

- **SAFE defaults**: `int`, `str`, `bool`, `None` (immutable types)
- **DANGEROUS defaults**: `list`, `dict`, `set` (mutable types)
- **ALWAYS use**: `default_factory=list/dict/set` for mutable types
**REMEMBER:**  
"Mutable defaults are shared, `default_factory` creates fresh copies for each object."


### How pydantic works with fastapi
Basically when the data is received pydantic checks the type and format of data with `basemodel` class and whenever there is a mismatch it will send the **`442 Unprocessable Entity`** without further execution this helps us save compute for invalid requests