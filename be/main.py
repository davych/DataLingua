import sys

def run_api():
    import uvicorn
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    run_api()
   
   