#!/bin/zsh

echo "Starting Resume AI..."

# Backend
echo "Starting backend on http://localhost:8000..."
source venv/bin/activate
uvicorn api.index:app --reload --host 0.0.0.0 --port 8000 &

# Frontend (wait 3s for backend CORS)
sleep 3
cd frontend
yarn start

# Note: Ctrl+C in each terminal to stop


