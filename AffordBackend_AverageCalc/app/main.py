from fastapi import FastAPI, HTTPException
from app.service import processNumberRequest

app = FastAPI()

@app.get("/numbers/{numberId}")
async def getNumbers(numberId: str):
    try:
        response = await processNumberRequest(numberId)
        return response
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
