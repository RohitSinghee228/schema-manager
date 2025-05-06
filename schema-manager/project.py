from datetime import datetime
from typing import Dict, List, Optional, Union

from pydantic import BaseModel, Field

from app.models.common import StatusEnum


class ProjectMemberModel(BaseModel):
    """Model for project member."""
    
    user_id: str
    role: str
    joined_at: datetime = Field(default_factory=datetime.utcnow)


class ProjectBase(BaseModel):
    """Base schema for project data."""
    
    title: str
    description: str
    tags: List[str] = Field(default_factory=list)
    status: StatusEnum = Field(default=StatusEnum.DRAFT)
    is_public: bool = False
    deadline: Optional[datetime] = None
    metadata: Dict[str, Union[str, int, bool, List[str]]] = Field(default_factory=dict)


class ProjectCreate(ProjectBase):
    """Schema for creating a new project."""
    
    members: List[Dict[str, str]] = Field(default_factory=list)
    related_ideas: List[str] = Field(default_factory=list)
    related_papers: List[str] = Field(default_factory=list)
    related_code_snippets: List[str] = Field(default_factory=list)


class ProjectUpdate(BaseModel):
    """Schema for updating a project."""
    
    title: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    status: Optional[StatusEnum] = None
    is_public: Optional[bool] = None
    deadline: Optional[datetime] = None
    metadata: Optional[Dict[str, Union[str, int, bool, List[str]]]] = None


class ProjectMemberResponse(BaseModel):
    """Schema for project member response data."""
    
    user_id: str
    role: str
    joined_at: datetime
    user_username: Optional[str] = None
    user_profile_picture: Optional[str] = None


class CommentResponse(BaseModel):
    """Schema for comment response data."""
    
    user_id: str
    content: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    user_username: Optional[str] = None


class ProjectResponse(ProjectBase):
    """Schema for project response data."""
    
    id: str
    user_id: str
    created_at: datetime
    updated_at: datetime
    likes: int
    views: int
    members: List[ProjectMemberResponse] = Field(default_factory=list)
    related_ideas: List[str] = Field(default_factory=list)
    related_papers: List[str] = Field(default_factory=list)
    related_code_snippets: List[str] = Field(default_factory=list)
    comments: List[CommentResponse] = Field(default_factory=list)


class ProjectWithUser(ProjectResponse):
    """Project response with user information."""
    
    user_username: str
    user_profile_picture: Optional[str] = None


class ProjectMemberUpdate(BaseModel):
    """Schema for updating project members."""
    
    members: List[Dict[str, str]]


class ProjectContentUpdate(BaseModel):
    """Schema for updating project related content."""
    
    operation: str  # "add" or "remove"
    content_type: str  # "idea", "paper", or "code_snippet"
    content_id: str


class ProjectCommentCreate(BaseModel):
    """Schema for creating a project comment."""
    
    content: str


class ProjectSearchParams(BaseModel):
    """Parameters for searching projects."""
    
    query: Optional[str] = None
    tags: Optional[List[str]] = None
    user_id: Optional[str] = None
    member_id: Optional[str] = None
    status: Optional[StatusEnum] = None
    is_public: Optional[bool] = None
    sort_by: str = "created_at"
    sort_order: str = "desc"
    limit: int = 10
    skip: int = 0 