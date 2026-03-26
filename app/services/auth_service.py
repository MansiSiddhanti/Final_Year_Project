def authenticate_user(payload: dict):
    username = payload.get("username")
    password = payload.get("password")

    if username == "admin" and password == "admin":
        return {"status": "success", "message": "Login successful"}
    
    return {"status": "failure", "message": "Invalid credentials"}
