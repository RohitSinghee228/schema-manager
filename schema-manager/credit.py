from datetime import datetime
from typing import Dict, Optional, Union

from pydantic import BaseModel, Field


class CreditBase(BaseModel):
    """Base schema for credit data."""
    
    amount: int
    description: str
    transaction_type: str
    related_entity_id: Optional[str] = None
    related_entity_type: Optional[str] = None
    payment_id: Optional[str] = None


class CreditCreate(CreditBase):
    """Schema for creating a new credit transaction."""
    
    user_id: str
    balance: int


class CreditResponse(CreditBase):
    """Schema for credit response data."""
    
    id: str
    user_id: str
    balance: int
    created_at: datetime
    updated_at: datetime


class CreditSummary(BaseModel):
    """Schema for credit summary data."""
    
    total_credits: int
    total_spent: int
    available_credits: int
    last_transaction: Optional[CreditResponse] = None


class CreditPurchase(BaseModel):
    """Schema for purchasing credits."""
    
    amount: int
    payment_method: str  # "stripe", "paypal", etc.
    payment_details: Dict[str, Union[str, int]] = Field(default_factory=dict)


class CreditUsage(BaseModel):
    """Schema for using credits."""
    
    amount: int
    description: str
    related_entity_id: Optional[str] = None
    related_entity_type: Optional[str] = None


class CreditSearchParams(BaseModel):
    """Parameters for searching credit transactions."""
    
    user_id: Optional[str] = None
    transaction_type: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    sort_by: str = "created_at"
    sort_order: str = "desc"
    limit: int = 10
    skip: int = 0 