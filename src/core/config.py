from datetime import timedelta

# ⚠️ DO NOT use this in production.
# Set SECRET_KEY via environment variable.
SECRET_KEY = "change-this-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE = timedelta(hours=1)
