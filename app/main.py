from fastapi import FastAPI, HTTPException

app = FastAPI()

users = {
    "1": {"id": 1, "name": "Mahdi", "role": "DevOps Engineer"},
    "2": {"id": 2, "name": "Sara", "role": "Backend Developer"},
    "3": {"id": 3, "name": "Youssef", "role": "Cloud Engineer"},
    "4": {"id": 4, "name": "Lina", "role": "Frontend Developer"},
    "5": {"id": 5, "name": "Adam", "role": "Security Analyst"},
}
@app.get("/user/{user_id}")
def get_user(user_id: str):
    if user_id in users:
        return users[user_id]
    raise HTTPException(status_code=404, detail="User not found")
