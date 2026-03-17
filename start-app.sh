#!/bin/zsh
echo "🚀 Starting Resume AI App..."
echo "Backend: http://localhost:8000"
echo "Frontend: http://localhost:3000"

# Kill existing servers
kill $(lsof -ti:8000) 2>/dev/null
kill $(lsof -ti:3000) 2>/dev/null
sleep 2

# Backend
source venv/bin/activate
uvicorn api.index:app --reload --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!
echo "Backend PID: $BACKEND_PID"

# Frontend
cd frontend
yarn start &
FRONTEND_PID=$!
echo "Frontend PID: $FRONTEND_PID"

# Open browser
sleep 5
open http://localhost:3000

echo "✅ App started! Press Ctrl+C to stop."
wait
