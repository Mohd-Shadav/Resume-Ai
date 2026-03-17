@app.post("/signup")
def signup(user: UserSignup):
    if user.email in users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    users_db[user.email] = {
        "password": user.password,
        "role": "job_seeker"
    }

    return {
        "message": "Signup successful",
        "token": "dummy-token",
        "user": {
            "email": user.email,
            "role": "job_seeker"
        }
    }


@app.post("/login")
def login(user: UserLogin):
    if user.email not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    if users_db[user.email]["password"] != user.password:
        raise HTTPException(status_code=401, detail="Invalid password")

    return {
        "message": "Login successful",
        "token": "dummy-token",
        "user": {
            "email": user.email,
            "role": users_db[user.email]["role"]
        }
    }