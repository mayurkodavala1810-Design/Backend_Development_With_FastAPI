"""
Hello API — Topic 1 Project
A minimal FastAPI backend to see the request lifecycle in action.

Run:
    pip install fastapi uvicorn
    uvicorn main:app --reload

Then open:
    http://127.0.0.1:8000/          -> basic hello
    http://127.0.0.1:8000/hello/Mayur -> personalized hello
    http://127.0.0.1:8000/docs      -> auto-generated Swagger UI (this is huge — explore it)
"""

from fastapi import FastAPI

app = FastAPI(title = "Hello API", version="1.0.0")


# GET / -> root endpoint. This is the "application server" logic
# that runs when a client (browser) sends an HTTP GET request.
@app.get("/")
def read_root():
    return{"message" : "Hello, Backend World...."}


# GET /hello/{name} -> path parameter example.
# Try /hello/Mayur in the browser and watch FastAPI parse the URL segment
# into a Python variable automatically.

@app.get("/hello/{name}")
def read_hello(name : str):
    return{"message" : f"Hello, {name}!, This Response came from the Backend."}


# GET /health -> a pattern you'll see in EVERY real backend.
# Load balancers and orchestrators (Kubernetes, Docker) ping this
# endpoint to check "is this server alive?" before routing traffic to it.

@app.get("/health")
def health_check():
    return{"status" : "ok"}