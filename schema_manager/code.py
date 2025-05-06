from datetime import datetime
from typing import Dict, List, Optional, Union

from beanie import PydanticObjectId
from pydantic import BaseModel, Field

from app.models.common import LanguageEnum


class CodeSnippetBase(BaseModel):
    """Base schema for code snippet data."""
    
    title: str
    description: Optional[str] = None
    code: str
    language: LanguageEnum = LanguageEnum.PYTHON
    tags: List[str] = Field(default_factory=list)
    is_public: bool = False
    metadata: Dict[str, Union[str, int, bool, List[str]]] = Field(default_factory=dict)


class CodeSnippetCreate(CodeSnippetBase):
    """Schema for creating a new code snippet."""
    
    ai_generated: bool = False
    ai_interaction_id: Optional[str] = None
    related_idea_id: Optional[str] = None
    related_project_id: Optional[str] = None


class CodeSnippetUpdate(BaseModel):
    """Schema for updating a code snippet."""
    
    title: Optional[str] = None
    description: Optional[str] = None
    code: Optional[str] = None
    language: Optional[LanguageEnum] = None
    tags: Optional[List[str]] = None
    is_public: Optional[bool] = None
    related_idea_id: Optional[str] = None
    related_project_id: Optional[str] = None
    metadata: Optional[Dict[str, Union[str, int, bool, List[str]]]] = None


class CodeSnippetResponse(CodeSnippetBase):
    """Schema for code snippet response data."""
    
    id: str
    user_id: str
    created_at: datetime
    updated_at: datetime
    likes: int
    views: int
    ai_generated: bool
    ai_interaction_id: Optional[str] = None
    related_idea_id: Optional[str] = None
    related_project_id: Optional[str] = None


class CodeSnippetWithUser(CodeSnippetResponse):
    """Code snippet response with user information."""
    
    user_username: str
    user_profile_picture: Optional[str] = None


class CodeSnippetSearchParams(BaseModel):
    """Parameters for searching code snippets."""
    
    query: Optional[str] = None
    language: Optional[LanguageEnum] = None
    tags: Optional[List[str]] = None
    user_id: Optional[str] = None
    is_public: Optional[bool] = None
    ai_generated: Optional[bool] = None
    related_idea_id: Optional[str] = None
    related_project_id: Optional[str] = None
    sort_by: str = "created_at"
    sort_order: str = "desc"
    limit: int = 10
    skip: int = 0 