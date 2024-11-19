@echo off

REM Backend setup and run
echo Setting up and starting the backend...
cd backend

REM Check if virtual environment exists; if not, create it
if not exist venv (
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate

REM Install dependencies
pip install -r requirements.txt

REM Run the backend
echo Starting the FastAPI backend...
start /B cmd /c "uvicorn main:app --host 127.0.0.1 --port 8000"

cd ..

REM Frontend setup and run
echo Setting up and starting the frontend...
cd frontend

REM Install Node.js dependencies
if not exist node_modules (
    npm install
)

REM Start the frontend development server
start /B cmd /c "npm run serve"

cd ..

echo Development environment is running.
echo Press any key to stop...
pause

REM Stopping services
taskkill /IM "uvicorn.exe" /F
taskkill /IM "node.exe" /F
echo Stopped all services.
