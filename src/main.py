from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

#import uvicorn
#uvicorn.run(app, host="0.0.0.0", port=8000)
