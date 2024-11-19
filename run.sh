#!/bin/bash

# Backend setup and run
echo "Setting up and starting the backend..."

cd backend

# Check if virtual environment exists; if not, create it
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
source ./venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the backend
echo "Starting the FastAPI backend..."
uvicorn main:app --host 127.0.0.1 --port 8000 &
BACKEND_PID=$!

cd ..

# Frontend setup and run
echo "Setting up and starting the frontend..."

cd frontend

# Install Node.js dependencies
if [ ! -d "node_modules" ]; then
    npm install
fi

# Start the frontend development server
npm run dev &
FRONTEND_PID=$!

# Wait for user input to stop services
echo "Press Ctrl+C to stop the development environment."

# Catch termination signal and clean up
trap "echo 'Stopping...'; kill $BACKEND_PID $FRONTEND_PID; exit 0" INT

wait
