from fastapi import FastAPI, HTTPException

app = FastAPI()

users = {
    "1": {"id": 1, "name": "Alice", "role": "admin"},
    "2": {"id": 2, "name": "Bob", "role": "user"},
    "3": {"id": 3, "name": "Charlie", "role": "guest"},
}

@app.get("/user/{user_id}")
def get_user(user_id: str):
    if user_id in users:
        return users[user_id]
    raise HTTPException(status_code=404, detail="User not found")
