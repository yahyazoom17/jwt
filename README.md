# FastAPI JWT Authentication

A secure and scalable RESTful API with JWT authentication built using FastAPI and MongoDB. This project provides user authentication and a contact management system with complete CRUD operations.

## Features

- 🔐 JWT-based authentication 
- 👤 User registration and login
- 📝 Complete contact management with CRUD operations
- 🛡️ Protected routes with token verification
- 📊 MongoDB integration for data persistence

## Tech Stack

- **FastAPI**: Modern, high-performance web framework for building APIs
- **MongoDB**: NoSQL database for storing user and contact information
- **Mongoengine**: MongoDB ODM for Python
- **JWT**: JSON Web Tokens for secure authentication
- **Python 3.9+**: Core programming language

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fastapi-jwt.git
   cd fastapi-jwt
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with the following variables:
   ```
   DB_HOST=your_mongodb_host_address
   DB_NAME=your_database_name
   ```

## Usage

1. Start the server:
   ```bash
   uvicorn server:app --reload
   ```

2. Access the API documentation at `http://localhost:8000/docs`

## API Endpoints

### Authentication

- **POST** `/signup`: Register a new user
  - Body: `{"name": "username", "email": "user@example.com", "password": "yourpassword"}`

- **POST** `/signin`: Sign in with existing credentials
  - Body: `{"email": "user@example.com", "password": "yourpassword"}`
  - Returns JWT token

### Contact Management

All contact endpoints require authentication with a valid JWT token in the Authorization header:
`Authorization: Bearer your_access_token`

- **POST** `/contacts/create`: Create a new contact
  - Body: `{"name": "Contact Name", "email": "contact@example.com", "phone": "+1234567890"}`

- **GET** `/contacts`: Get all contacts for logged-in user

- **GET** `/contacts/{contact_id}`: Get a specific contact by ID

- **PUT** `/contacts/update/{contact_id}`: Update a specific contact
  - Body: `{"name": "Updated Name", "email": "updated@example.com", "phone": "+0987654321"}`

- **DELETE** `/contacts/delete/{contact_id}`: Delete a specific contact

## Data Models

### User
- `user_id`: Unique identifier (UUID)
- `name`: User's name
- `email`: User's email (unique)
- `password`: User's password
- `created_at`: Timestamp of creation
- `updated_at`: Timestamp of last update

### Contact
- `contact_id`: Unique identifier (UUID)
- `name`: Contact's name
- `email`: Contact's email (unique)
- `phone`: Contact's phone number (unique)
- `user`: Reference to the user who created the contact
- `created_at`: Timestamp of creation
- `updated_at`: Timestamp of last update

## JWT Authentication Flow

1. User registers with `/signup` or logs in with `/signin`
2. Server returns a JWT token upon successful authentication
3. Client includes the token in the Authorization header for subsequent requests
4. Protected routes verify the token before processing the request

## Development

The project structure is organized as follows:

```
fastapi-jwt/
├── contacts.py       # Contact routes and handlers
├── database.py       # Database connection and operations
├── jwtsign.py        # JWT token management
├── models.py         # Data models
├── server.py         # Main application entry point
├── requirements.txt  # Project dependencies
└── .env              # Environment variables (create this file)
```

## Security Notes

- Tokens expire after 20 minutes by default
- Raw passwords are currently stored in the database - in a production environment, implement proper password hashing
- JWT secret is generated using `secrets.token_hex(16)` - consider using a persistent secret in production
- 
