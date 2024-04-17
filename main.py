from fastapi import FastAPI
from routes import clone  # add here

app = FastAPI()


# router pages #add here
app.include_router(clone.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000)
