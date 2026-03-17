import os
from typing import Dict, List, Optional
from datetime import datetime
import uuid
from dotenv import load_dotenv

load_dotenv()

# In-memory stores (fallback, replace with Mongo in prod)
users: Dict[str, dict] = {}
jobs: Dict[str, dict] = {}
resumes: Dict[str, dict] = {}
applications: Dict[str, dict] = {}

class Database:
    @staticmethod
    def get_user(user_id: str) -> Optional[dict]:
        return users.get(user_id)

    @staticmethod
    def create_user(user_data: dict) -> str:
        user_id = str(uuid.uuid4())
        user_data.update({'id': user_id, 'created_at': datetime.utcnow()})
        users[user_id] = user_data
        return user_id

    @staticmethod
    def get_jobs(employer_id: Optional[str] = None) -> List[dict]:
        if employer_id:
            return [j for j in jobs.values() if j['employer_id'] == employer_id]
        return list(jobs.values())

    @staticmethod
    def create_job(job_data: dict, employer_id: str) -> str:
        job_id = str(uuid.uuid4())
        job_data.update({'id': job_id, 'employer_id': employer_id, 'created_at': datetime.utcnow()})
        jobs[job_id] = job_data
        return job_id

    @staticmethod
    def get_job(job_id: str) -> Optional[dict]:
        return jobs.get(job_id)

    @staticmethod
    def get_resumes(user_id: str) -> List[dict]:
        return [r for r in resumes.values() if r['user_id'] == user_id]

    @staticmethod
    def create_resume(resume_data: dict, user_id: str) -> str:
        resume_id = str(uuid.uuid4())
        resume_data.update({'id': resume_id, 'user_id': user_id, 'created_at': datetime.utcnow()})
        resumes[resume_id] = resume_data
        return resume_id

    @staticmethod
    def create_application(app_data: dict, user_id: str) -> str:
        app_id = str(uuid.uuid4())
        app_data.update({'id': app_id, 'user_id': user_id, 'status': 'pending', 'created_at': datetime.utcnow()})
        applications[app_id] = app_data
        return app_id

db = Database()

