## encrypted-password-vault-api

A Python-based backend API for securely storing and retrieving encrypted credentials.
The service uses modern password hashing, symmetric encryption, and JWT-based authentication
to protect sensitive data at rest and in transit.

This project was built as a learning exercise to understand backend API design,
authentication, cryptography best practices, and secure data storage using Python
and FastAPI.

--------------------------------------------------------------------------------------------------------

## WHAT THIS PROJECT DOES

This backend provides a secure API for managing encrypted credential entries.

It allows a client to:
```
• Authenticate using a master password
• Hash passwords securely using Argon2
• Encrypt stored credentials before saving them to the database
• Store encrypted entries in a SQLite database
• Retrieve and decrypt entries only after authentication
• Use JWT access tokens to protect API routes
```
--------------------------------------------------------------------------------------------------------

## HOW IT WORKS (HIGH LEVEL)
```
• The application starts a FastAPI server
• A master password is hashed and verified using Argon2
• Upon successful authentication, a JWT access token is issued
• Protected endpoints require a valid JWT
• Credential values are encrypted using symmetric encryption before storage
• Encrypted data and salts are stored in SQLite
• Data is decrypted only when explicitly requested
```
--------------------------------------------------------------------------------------------------------

PROJECT STRUCTURE
```
encrypted-password-vault-api/
├── src/
│   ├── api/
│   │   ├── auth.py          - Authentication routes
│   │   ├── entries.py       - Credential entry routes
│   │   └── health.py        - Health check endpoint
│   │
│   ├── core/
│   │   ├── config.py        - App configuration and constants
│   │   ├── crypto.py        - Encryption / decryption utilities
│   │   └── security.py     - Password hashing and JWT helpers
│   │
│   ├── database/
│   │   ├── init_db.py       - Database initialization
│   │   ├── models.py        - SQLAlchemy models
│   │   └── session.py       - Database session handling
│   │
│   ├── schemas/
│   │   ├── auth.py          - Pydantic auth schemas
│   │   └── entries.py       - Pydantic entry schemas
│   │
│   ├── services/
│   │   └── vault.py         - Core vault logic
│   │
│   └── deps.py              - Dependency injection helpers
│
├── main.py                  - Application entry point
├── requirements.txt
├── .gitignore
├── README.txt
```
--------------------------------------------------------------------------------------------------------

## FILE EXPLANATIONS

main.py

This is the main entry point of the application.

It is responsible for:
```
• Creating the FastAPI application
• Initializing the database on startup
• Registering API routers
• Launching the server
```
--------------------------------------------------------------------------------------------------------

## src/api/auth.py

Handles authentication-related routes.

This file:
```
• Verifies the master password
• Issues JWT access tokens
• Acts as the authentication gateway for the API
```
--------------------------------------------------------------------------------------------------------

## src/api/entries.py

Handles credential entry routes.

This file:
```
• Creates encrypted credential entries
• Lists stored entries
• Reveals (decrypts) a specific entry when authorized
```
--------------------------------------------------------------------------------------------------------

## src/core/security.py

Handles authentication and password security.

This file:
```
• Hashes passwords using Argon2
• Verifies hashed passwords
• Creates and signs JWT access tokens
```
--------------------------------------------------------------------------------------------------------

## src/core/crypto.py

Handles encryption logic.

This file:
```
• Derives encryption keys
• Encrypts credential values before storage
• Decrypts credential values on retrieval
```
--------------------------------------------------------------------------------------------------------

## src/database/models.py

Defines database models.

This file:
```
• Defines the credential entry schema
• Stores encrypted values and salts
• Uses SQLAlchemy ORM for database interaction
```
--------------------------------------------------------------------------------------------------------

## INSTALLATION / PROCESS

Clone the repository:
```
git clone https://github.com/YOUR_USERNAME/encrypted-password-vault-api.git
cd encrypted-password-vault-api
```
--------------------------------------------------------------------------------------------------------

## INSTALL DEPENDENCIES:
```
pip install -r requirements.txt
```
--------------------------------------------------------------------------------------------------------

## RUN THE SERVER:
```
uvicorn main:app --reload
```
--------------------------------------------------------------------------------------------------------

## OUTPUT
```
• A FastAPI server is started locally
• SQLite database is created automatically if missing
• Encrypted credential entries are stored securely
• Decryption is only performed on authorized requests
```
--------------------------------------------------------------------------------------------------------

## CONFIGURATION AND SECURITY NOTES
```
• This project runs locally by default
• SQLite database files are generated at runtime and should not be committed
• The SECRET_KEY value in config.py is a placeholder
• SECRET_KEY must be replaced via environment variable in production
• JWT tokens are signed using the configured algorithm
• This project is intended for educational and learning purposes
```
--------------------------------------------------------------------------------------------------------

## NOTES AND LIMITATIONS
```
• This is a backend-only service (no frontend included)
• Authentication is simplified for learning purposes
• Multi-user support is not implemented
• SQLite is used for simplicity, not scalability
• This project is not production-hardened
```
--------------------------------------------------------------------------------------------------------

## LICENSE

This project is provided for educational and personal use.
