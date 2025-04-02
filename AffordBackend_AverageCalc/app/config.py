import os

class Config:
    windowSize = int(os.getenv("WINDOW_SIZE", 10))
    apiBaseUrl = "http://20.244.56.144/evaluation-service"
    timeout = 500 
    clientID = "24f2a94b-7877-44fa-a70e-623d41277b28"
    clientSecret = "EjZhaTvXNGeaZARM"
    accessToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzQzNjAwNjg3LCJpYXQiOjE3NDM2MDAzODcsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6IjI0ZjJhOTRiLTc4NzctNDRmYS1hNzBlLTYyM2Q0MTI3N2IyOCIsInN1YiI6IjIyMjgwNDBAa2lpdC5hYy5pbiJ9LCJlbWFpbCI6IjIyMjgwNDBAa2lpdC5hYy5pbiIsIm5hbWUiOiJwcmFuYXYga3VtYXIiLCJyb2xsTm8iOiIyMjI4MDQwIiwiYWNjZXNzQ29kZSI6Im53cHdyWiIsImNsaWVudElEIjoiMjRmMmE5NGItNzg3Ny00NGZhLWE3MGUtNjIzZDQxMjc3YjI4IiwiY2xpZW50U2VjcmV0IjoiRWpaaGFUdlhOR2VhWkFSTSJ9.xVrHb2D1GMohmKHw46NnisdN2q-BDJrsujuL3j_wchI"
    authHeader = {"Authorization": f"Bearer {accessToken}"}

config = Config()
