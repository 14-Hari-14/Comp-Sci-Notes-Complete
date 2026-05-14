Date: 2025-12-12
Topics: #uvicorn #asgi #backend
Link: 
Class: [[]]

---

Before understanding uvicorn its important to understand `ASGI` which is shorthand for **Asynchronous Server Gateway Interface** 

# ASGI

ASGI is a specification that defines how a python web server communicates with a python web application

|**Feature**|**WSGI (Older Standard)**|**ASGI (Modern Standard)**|
|---|---|---|
|**Nature**|**Synchronous**. Handles one request at a time.|**Asynchronous**. Allows concurrent handling of multiple requests.|
|**Protocols**|Limited to **HTTP/1.1**.|Supports **HTTP/1.1, HTTP/2, and WebSockets**.|
|**Use Case**|Traditional web apps (blogs, simple APIs).|High-concurrency, real-time apps (chat, live notifications, ML APIs).|

### Example of ASGI packet

```json
# FastAPI doesn't see this raw HTTP:
# GET /users HTTP/1.1
# Host: example.com
# Content-Type: application/json

# FastAPI receives this ASGI format:
{
    'type': 'http.request',
    'scope': {
        'type': 'http',
        'method': 'GET',
        'path': '/users',
        'headers': [
            (b'host', b'example.com'),
            (b'content-type', b'application/json')
        ]
    },
    'body': b''
}
```

# Uvicorn

Its a very fast ASGI server implementation for python. Its like a glue between fastapi and https requests.

## Working 
1. Take the raw https request from streamlit
2. Convert it into a format that is ASGI compliant so that fastapi is able to understand the request 
3. Get the response from fastapi and convert it back into https request so that streamlit can display it


### Why FastAPI Can't Directly Handle HTTP:

**Technical Limitations:**
1. **HTTP is Low-Level**: Requires socket management, protocol parsing
2. **Async Complexity**: HTTP/1.1, HTTP/2, WebSockets need different handling
3. **Performance**: HTTP parsing is CPU-intensive, better done by specialized servers

Therefore uvicorn does the following 
 1. Parse HTTP headers
 2. Handle chunked encoding
 3. Manage keep-alive connections
 4. Handle SSL(**secure sockets layer**) /TLS (**transport layer security**) (if HTTPS)  
 5. Convert to ASGI format
 6. Send to FastAPI



