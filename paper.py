from datetime import datetime
from typing import Dict, List, Optional, Union

from beanie import PydanticObjectId
from pydantic import BaseModel, Field

from app.models import Comment, Reference
from app.models.common import StatusEnum


class PaperBase(BaseModel):
    """Base schema for paper data."""
    
    title: str
    abstract: str
    content: str
    tags: List[str] = Field(default_factory=list)
    status: StatusEnum = Field(default=StatusEnum.DRAFT)
    is_public: bool = False
    references: List[Reference] = Field(default_factory=list)
    metadata: Dict[str, Union[str, int, bool, List[str]]] = Field(default_factory=dict)


class PaperCreate(PaperBase):
    """Schema for creating a new paper."""
    
    ai_generated: bool = False
    ai_interaction_id: Optional[str] = None


class PaperUpdate(BaseModel):
    """Schema for updating a paper."""
    
    title: Optional[str] = None
    abstract: Optional[str] = None
    content: Optional[str] = None
    tags: Optional[List[str]] = None
    status: Optional[StatusEnum] = None
    is_public: Optional[bool] = None
    references: Optional[List[Reference]] = None
    metadata: Optional[Dict[str, Union[str, int, bool, List[str]]]] = None


class CommentCreate(BaseModel):
    """Schema for creating a comment."""
    
    content: str


class CommentResponse(BaseModel):
    """Schema for comment response data."""
    
    user_id: str
    content: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    is_deleted: bool = False
    user_username: Optional[str] = None
    user_profile_picture: Optional[str] = None


class PaperResponse(PaperBase):
    """Schema for paper response data."""
    
    id: str
    user_id: str
    created_at: datetime
    updated_at: datetime
    likes: int
    views: int
    ai_generated: bool
    ai_interaction_id: Optional[str] = None
    comments: List[CommentResponse] = Field(default_factory=list)


class PaperWithUser(PaperResponse):
    """Paper response with user information."""
    
    user_username: str
    user_profile_picture: Optional[str] = None


class PaperSearchParams(BaseModel):
    """Parameters for searching papers."""
    
    query: Optional[str] = None
    tags: Optional[List[str]] = None
    user_id: Optional[str] = None
    status: Optional[StatusEnum] = None
    is_public: Optional[bool] = None
    ai_generated: Optional[bool] = None
    sort_by: str = "created_at"
    sort_order: str = "desc"
    limit: int = 10
    skip: int = 0 