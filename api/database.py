import json
import uuid
from typing import Dict, List, Optional
from datetime import datetime
from pathlib import Path

# =========================
# 📁 FILE PATHS
# =========================
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

USERS_FILE = DATA_DIR / "users.json"
JOBS_FILE = DATA_DIR / "jobs.json"
RESUMES_FILE = DATA_DIR / "resumes.json"
APPLICATIONS_FILE = DATA_DIR / "applications.json"

# =========================
# 🧠 IN-MEMORY STORE
# =========================
users: Dict[str, dict] = {}
jobs: Dict[str, dict] = {}
resumes: Dict[str, dict] = {}
applications: Dict[str, dict] = {}

# =========================
# 💾 LOAD / SAVE HELPERS
# =========================
def load_data(file_path):
    if file_path.exists():
        with open(file_path, "r") as f:
            return json.load(f)
    return {}

def save_data(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, default=str, indent=2)

def load_all():
    global users, jobs, resumes, applications
    users = load_data(USERS_FILE)
    jobs = load_data(JOBS_FILE)
    resumes = load_data(RESUMES_FILE)
    applications = load_data(APPLICATIONS_FILE)

def save_all():
    save_data(USERS_FILE, users)
    save_data(JOBS_FILE, jobs)
    save_data(RESUMES_FILE, resumes)
    save_data(APPLICATIONS_FILE, applications)

# 🔥 LOAD DATA AT START
load_all()

# =========================
# 🗄️ DATABASE CLASS
# =========================
class Database:

    # 👤 USERS
    @staticmethod
    def get_user(user_id: str) -> Optional[dict]:
        return users.get(user_id)

    @staticmethod
    def create_user(user_data: dict) -> str:
        user_id = str(uuid.uuid4())
        user_data.update({
            'id': user_id,
            'created_at': datetime.utcnow().isoformat()
        })
        users[user_id] = user_data
        save_all()
        return user_id

    # 💼 JOBS
    @staticmethod
    def get_jobs(employer_id: Optional[str] = None) -> List[dict]:
        if employer_id:
            return [j for j in jobs.values() if j['employer_id'] == employer_id]
        return list(jobs.values())

    @staticmethod
    def create_job(job_data: dict, employer_id: str) -> str:
        job_id = str(uuid.uuid4())
        job_data.update({
            'id': job_id,
            'employer_id': employer_id,
            'created_at': datetime.utcnow().isoformat()
        })
        jobs[job_id] = job_data
        save_all()
        return job_id

    @staticmethod
    def get_job(job_id: str) -> Optional[dict]:
        return jobs.get(job_id)

    # 📄 RESUMES
    @staticmethod
    def get_resumes(user_id: str) -> List[dict]:
        return [r for r in resumes.values() if r['user_id'] == user_id]

    @staticmethod
    def create_resume(resume_data: dict, user_id: str) -> str:
        resume_id = str(uuid.uuid4())
        resume_data.update({
            'id': resume_id,
            'user_id': user_id,
            'created_at': datetime.utcnow().isoformat()
        })
        resumes[resume_id] = resume_data
        save_all()
        return resume_id

    # 📌 APPLICATIONS
    @staticmethod
    def create_application(app_data: dict, user_id: str) -> str:
        app_id = str(uuid.uuid4())
        app_data.update({
            'id': app_id,
            'user_id': user_id,
            'status': 'pending',
            'created_at': datetime.utcnow().isoformat()
        })
        applications[app_id] = app_data
        save_all()
        return app_id


# 🔗 INSTANCE
db = Database()