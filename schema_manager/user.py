from datetime import datetime
from typing import Dict, List, Optional, Union

from pydantic import BaseModel, EmailStr, Field, validator


class UserBase(BaseModel):
    """Base schema for user data."""
    
    email: EmailStr
    username: str
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    profile_picture: Optional[str] = None
    bio: Optional[str] = None


class UserCreate(UserBase):
    """Schema for creating a new user."""
    
    password: str = Field(..., min_length=8)
    
    @validator('password')
    def password_strength(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not any(c.isupper() for c in v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(c.islower() for c in v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not any(c.isdigit() for c in v):
            raise ValueError('Password must contain at least one number')
        return v


class SocialUserCreate(UserBase):
    """Schema for creating a user via social login.
    Password is optional because social logins may not provide one.
    """

    password: Optional[str] = None
    social_provider: Optional[str] = None


class UserUpdate(BaseModel):
    """Schema for updating user information."""
    
    username: Optional[str] = None
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    bio: Optional[str] = None
    profile_picture: Optional[str] = None
    preferences: Optional[Dict[str, Union[str, int, bool, List[str]]]] = None


class UserPasswordUpdate(BaseModel):
    """Schema for updating a user's password."""
    
    current_password: str
    new_password: str = Field(..., min_length=8)
    
    @validator('new_password')
    def password_strength(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not any(c.isupper() for c in v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(c.islower() for c in v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not any(c.isdigit() for c in v):
            raise ValueError('Password must contain at least one number')
        return v


class UserPreferencesUpdate(BaseModel):
    """Schema for updating user preferences."""
    
    preferences: Dict[str, Union[str, int, bool, List[str]]]


class UserResponse(UserBase):
    """Schema for user response data."""
    
    id: str
    is_active: bool
    is_verified: bool
    credits: int
    created_at: datetime
    updated_at: datetime
    last_login: Optional[datetime] = None
    
    class Config:
        """Pydantic config."""
        orm_mode = True


class UserLogin(BaseModel):
    """Schema for user login."""
    
    email: EmailStr
    password: str


class PasswordResetRequest(BaseModel):
    """Schema for requesting a password reset."""
    
    email: EmailStr


class PasswordReset(BaseModel):
    """Schema for resetting a password."""
    
    token: str
    new_password: str = Field(..., min_length=8)
    
    @validator('new_password')
    def password_strength(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not any(c.isupper() for c in v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(c.islower() for c in v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not any(c.isdigit() for c in v):
            raise ValueError('Password must contain at least one number')
        return v


class EmailVerification(BaseModel):
    """Schema for email verification."""
    
    token: str


class UserWithStats(UserResponse):
    """User response with additional statistics."""
    
    idea_count: int = 0
    paper_count: int = 0
    code_snippet_count: int = 0
    project_count: int = 0
    total_credits: int = 0


class User(BaseModel):
    id: str
    email: str = None
    is_active: bool = True

    class Config:
        orm_mode = True


class UserSignupResponse(BaseModel):
    """Simplified schema for user signup response."""
    
    id: str
    email: str
    username: str
    full_name: Optional[str] = None
    
    class Config:
        """Pydantic config."""
        orm_mode = True 