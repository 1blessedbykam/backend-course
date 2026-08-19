from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Clouned First API")

users = []


class RegisterRequest(BaseModel):
    username: str
    password: str
    age: int


@app.get("/")
def home():
    return {"message": "Hello from Clouned backend API"}


@app.get("/users")
def get_users():
    return {
        "users": users
    }


@app.get("/users/{username}")
def get_user(username: str):
    for user in users:
        if user["username"] == username:
            return {
                "found": True,
                "user": {
                    "username": "Clouned",
                    "age": 15   
                }
            }

    return {
        "success": False,
        "message": "User not found"
    }


def validate_username(username):
    return len(username) >= 3


def validate_password(password):
    return len(password) >= 8


def validate_age(age):
    return 13 <= age <= 100


def username_exists(username):
    for user in users:
        if user["username"] == username:
            return True
    return False


@app.post("/register")
def register(data: RegisterRequest):
    errors = []

    if not validate_username(data.username):
        errors.append("Username must be at least 3 characters.")

    if not validate_password(data.password):
        errors.append("Password must be at least 8 characters.")

    if not validate_age(data.age):
        errors.append("Age must be between 13 and 100.")

    if username_exists(data.username):
        errors.append("Username already exists.")

    if len(errors) > 0:
        return {
            "success": False,
            "errors": errors
        }

    users.append({
        "username": data.username,
        "age": data.age
    })

    return {
        "success": True,
        "message": f"Account created for {data.username}"
    }


@app.get("/about")
def about():
    return {
        "name": "Clouned",
        "age": 15,
        "path": "Backend Engineering"
    }

@app.get("/multiply")
def multiply(a: int, b: int):
    return {"result": a * b}

@app.get("/my-skills")
def my_skills():
    return {
        "skills": ["Python",
                    "Git",
                    "JSON"
                    "FastAPI"
        ]
    }

@app.get("/status")
def status():
    return {
        "status": "online",
        "developper": "Clouned",
        "level": "training backend engineer"
    }