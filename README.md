# Google React App

This project is a full-stack application that includes both a backend and a frontend. The backend is built with Node.js/Express, and the frontend is built with React.

## Features
- Backend API for handling data and business logic.
- Frontend React application for user interaction.
- Seamless integration between backend and frontend.

## Folder Structure
```
google-react-app/
├── backend/       # Backend code (FastAPI)
├── frontend/      # Frontend code (React)
└── README.md      # Project documentation
```

## Prerequisites
- Node.js (v14 or higher)
- npm or yarn
- Git (optional)
- Fastapi & uvicorn

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Rajkumar-21/google-books-react-fastapi-app.git
cd google-books-react-fastapi-app
```

### 2. Backend Setup
1. Navigate to the `backend` folder:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   python -m venv env
   pip install -r requirements.txt
   ```
3. Start the backend server:
   ```bash
   uvicorn main:app --reload
   ```
   The backend server will run on `http://localhost:8000` by default.

### 3. Frontend Setup
1. Navigate to the `frontend` folder:
   ```bash
   cd ../frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the frontend development server:
   ```bash
   npm start
   ```
   The frontend application will run on `http://localhost:3000` by default.

## Running the Application
1. Start the backend server as described in the Backend Setup section.
2. Start the frontend server as described in the Frontend Setup section.
3. Open your browser and navigate to `http://localhost:3000` to access the application.

## Environment Variables
- Backend: Create a `.env` file in the `backend` folder to configure environment variables (e.g., database connection strings, API keys).
- Frontend: Create a `.env` file in the `frontend` folder to configure environment variables (e.g., API base URL).

## Additional Notes
- Ensure that the backend and frontend are properly connected by updating the API base URL in the frontend configuration.
- For production deployment, build the frontend and serve it using the backend.

## License
This project is licensed under the MIT License.
