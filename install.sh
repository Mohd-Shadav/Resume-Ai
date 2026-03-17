#!/bin/zsh

echo "Installing Resume AI dependencies (macOS)..."

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "Python3 not found. Install from https://www.python.org"
    exit 1
fi

# Create virtual env
python3 -m venv venv
source venv/bin/activate

# Backend deps
pip install -r requirements.txt

# Frontend: Node/Yarn
if ! command -v node &> /dev/null; then
    echo "Node.js not found. Install from https://nodejs.org"
    exit 1
fi

if ! command -v yarn &> /dev/null; then
    npm install -g yarn
fi

cd frontend
yarn install
cd ..

echo "✅ Installation complete! Run ./run.sh to start."
echo "Backend: http://localhost:8000 | Frontend: http://localhost:3000"

