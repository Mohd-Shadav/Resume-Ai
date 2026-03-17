from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
import uuid

class UserBase(BaseModel):
    email: EmailStr
    name: str
    role: str  # 'job_seeker' or 'employer'

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: str
    created_at: datetime

    class Config:
        from_attributes = True

class JobBase(BaseModel):
    title: str
    company: str
    location: str
    job_type: str
    description: str
    requirements: List[str]
    salary_range: Optional[str] = None

class JobCreate(JobBase):
    pass

class JobOut(JobBase):
    id: str
    employer_id: str
    created_at: datetime

    class Config:
        from_attributes = True

class ResumeBase(BaseModel):
    filename: str
    content: str  # Extracted text

class ResumeCreate(ResumeBase):
    pass

class ResumeOut(ResumeBase):
    id: str
    user_id: str
    created_at: datetime

    class Config:
        from_attributes = True

class ApplicationCreate(BaseModel):
    job_id: str
    resume_id: str

class ApplicationOut(BaseModel):
    id: str
    job_id: str
    resume_id: str
    user_id: str
    status: str = 'pending'
    created_at: datetime

    class Config:
        from_attributes = True

