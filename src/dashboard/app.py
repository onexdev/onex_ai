from fastapi import FastAPI

app = FastAPI()

@app.get("/scan/{contract_address}")
async def scan(contract_address: str):
    return {"address": contract_address, "score": 0}
