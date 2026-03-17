# Resume AI - Working Website

## Quick Start

### macOS/Linux
```bash
chmod +x install.sh run.sh start-app.sh
./install.sh
./start-app.sh
```

### Windows
```cmd
install.bat
run.bat
```

**OS Detection:** Backend exposes `/api/os` endpoint showing server OS (e.g., {"os": "Darwin", "version": "23.6.0", ...}).

```bash
# Make executable
chmod +x install.sh run.sh

# Install deps (Python venv + yarn)
./install.sh

# Run both backend & frontend
./run.sh
```

**Backend:** http://localhost:8000/api/health  
**Frontend:** http://localhost:3000

## Features
- AI Resume/Job matching backend (FastAPI, in-memory DB ready for Mongo)
- Auth (signup/login JWT)
- Jobs CRUD
- Resumes upload
- Applications
- React frontend with shadcn UI

## Test Backend
```bash
curl http://localhost:8000/api/health
# Signup
curl -X POST http://localhost:8000/api/auth/signup -H "Content-Type: application/json" -d '{"email":"test@test.com","password":"test123","name":"Test","role":"job_seeker"}'
```

Website ready!
