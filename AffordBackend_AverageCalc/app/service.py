import httpx
from fastapi import HTTPException
from app.config import config

async def processNumberRequest(numberId: str):
    validIds = ['primes', 'fibonacci', 'even', 'random']
    if numberId not in validIds:
        raise HTTPException(status_code=400, detail="Invalid numberId")

    numbers = await fetchNumbers(numberId)
    storedNumbers = numbers[:config.windowSize]
    avg = sum(storedNumbers) / len(storedNumbers) if storedNumbers else 0
    return {
        "windowPrevState": [],
        "windowCurrState": storedNumbers,
        "numbers": storedNumbers,
        "avg": avg
    }

async def fetchNumbers(numberId: str):
    urlMapping = {
        'primes': '/primes',
        'fibonacci': '/fibo',
        'even': '/even',
        'random': '/rand'
    }

    url = f"{config.apiBaseUrl}{urlMapping.get(numberId)}"

    # Debugging: Print request details
    print(f"Fetching numbers from: {url}")
    print(f"Authorization Header: {config.authHeader}")

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                url, 
                headers={"Authorization": f"Bearer {config.accessToken}"}, 
                timeout=config.timeout / 1000
            )
            response.raise_for_status()
            return response.json().get("numbers", [])
        except httpx.RequestError as e:
            raise HTTPException(status_code=500, detail=f"Request failed: {e}")
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=f"HTTP error: {e}")
