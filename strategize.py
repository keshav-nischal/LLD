from abc import ABC, abstractmethod

class AuthStrategy(ABC):
    @abstractmethod
    def authenticate(self, request_data):
        pass

class EmailPasswordAuth(AuthStrategy):
    def authenticate(self, request_data):
        email = request_data.get("email")
        password = request_data.get("password")
        # TODO: Add DB lookup + password hash check
        if email == "test@example.com" and password == "123456":
            return {"status": "success", "user_id": 1}
        return {"status": "fail", "reason": "Invalid credentials"}

class GoogleAuth(AuthStrategy):
    def authenticate(self, request_data):
        token = request_data.get("google_token")
        # TODO: Use Google API to verify token
        if token == "valid_token":
            return {"status": "success", "user_id": 99}
        return {"status": "fail", "reason": "Invalid token"}

class AuthContext:
    def __init__(self, strategy: AuthStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: AuthStrategy):
        self.strategy = strategy

    def login(self, request_data):
        return self.strategy.authenticate(request_data)

# Email login
context = AuthContext(EmailPasswordAuth())
result = context.login({"email": "test@example.com", "password": "123456"})
print(result)

# Switch to Google login
context.set_strategy(GoogleAuth())
result = context.login({"google_token": "valid_token"})
print(result)
