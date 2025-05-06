from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class ResponseStatus(BaseModel):
    """API response status."""
    
    success: bool
    message: str
    code: int = 200


class PaginationParams(BaseModel):
    """Common pagination parameters."""
    
    page: int = Field(1, gt=0)
    limit: int = Field(10, gt=0, le=100)
    sort_by: Optional[str] = None
    sort_order: Optional[str] = "desc"


class PaginatedResponse(GenericModel, Generic[T]):
    """Generic paginated response model."""
    
    status: ResponseStatus
    data: List[T]
    page: int
    limit: int
    total: int
    total_pages: int


class StandardResponse(GenericModel, Generic[T]):
    """Generic standard response model."""
    
    status: ResponseStatus
    data: T


class ErrorResponse(BaseModel):
    """Error response model."""
    
    status: ResponseStatus
    error: Optional[Dict[str, Any]] = None


class SearchParams(BaseModel):
    """Common search parameters."""
    
    query: Optional[str] = None
    tags: Optional[List[str]] = None
    sort_by: Optional[str] = "created_at"
    sort_order: Optional[str] = "desc"
    limit: int = Field(10, gt=0, le=100)
    page: int = Field(1, gt=0) 