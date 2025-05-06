from pydantic import BaseModel, Field
from typing import Optional, List, Dict
import uuid

class IdeaGenerationTask(BaseModel):
    task_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    user_id: Optional[str] = "unknown"
    task_description: str
    code: Optional[str] = ""
    num_ideas: int
    num_reflections: int = 2
    prev_ideas: Optional[List[Dict]] = []
    seed_ideas: Optional[List[Dict]] = []
    system_prompt: Optional[str] = ""

class IdeaResponse(BaseModel):
    task_id: str
    user_id: str
    status: str
    task_description: str = ""
    thought: str = ""
    ideas: List[Dict] = []
    reflection_rounds: int = 1
    error: Optional[str] = None


class IdeaPromptSchema(BaseModel):
    Name: str = Field(description="The unique name for the idea.")
    Title: str = Field(description="A brief title for the idea.")
    Experiment: str = Field(description="Description of the experimental approach.")
    Interestingness: float = Field(description="How interesting the idea is.")
    Feasibility: float = Field(description="Feasibility rating (1-10 or qualitative).")
    Novelty: float = Field(description="Novelty rating (1-10 or qualitative).")


class IdeaTasksResponse(BaseModel):
    id: str
    task_id: str
    user_id: str
    status: str
    task_description: str
    thought: Optional[str] = None
    ideas: Optional[List[Dict]] = None
    reflection_rounds: Optional[int] = None
    error: Optional[str] = None
    tags: Optional[List[str]] = None
    metadata: Optional[dict] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    is_public: Optional[bool] = None