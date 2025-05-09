from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Union
import uuid
from datetime import datetime

class SimilarPaper(BaseModel):
    """Schema for similar paper information."""
    title: str = Field(description="Title of the paper")
    abstract: Optional[str] = Field(description="Abstract of the paper")
    authors: List[str] = Field(default_factory=list, description="List of authors")
    year: Optional[int] = Field(description="Publication year")
    source: str = Field(description="Source of the paper (e.g., 'arXiv', 'Semantic Scholar', 'Journal')")
    source_url: str = Field(description="URL to the paper in its source")
    journal: Optional[str] = Field(description="Journal name if published in a journal")
    doi: Optional[str] = Field(description="Digital Object Identifier if available")
    semantic_similarity: float = Field(description="Semantic similarity score with the generated idea")
    citations: Optional[int] = Field(description="Number of citations")
    venue: Optional[str] = Field(description="Conference or journal venue")
    keywords: List[str] = Field(default_factory=list, description="Keywords associated with the paper")
    pdf_url: Optional[str] = Field(description="Direct link to PDF if available")
    icon: Optional[str] = Field(description="Icon URL for the source (e.g., arXiv logo, journal logo)")

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
    tags: Optional[List[str]] = None
    metadata: Optional[dict] = None
    similar_papers: Optional[List[SimilarPaper]] = Field(default_factory=list, description="List of similar papers with comprehensive information")

class IdeaPromptSchema(BaseModel):
    Name: str = Field(description="The unique name for the idea.")
    Title: str = Field(description="A brief title for the idea.")
    Experiment: str = Field(description="Description of the experimental approach.")
    Interestingness: float = Field(description="How interesting the idea is.")
    Feasibility: float = Field(description="Feasibility rating (1-10 or qualitative).")
    Novelty: float = Field(description="Novelty rating (1-10 or qualitative).")
    description: str = Field(description="A comprehensive description that explains the research idea in detail.")
    implementation_steps: List[str] = Field(default_factory=list, description="Detailed step-by-step implementation plan.")
    expected_outcomes: List[str] = Field(default_factory=list, description="Expected results and outcomes of the idea.")
    potential_challenges: List[str] = Field(default_factory=list, description="Potential obstacles and challenges.")
    mitigation_strategies: List[str] = Field(default_factory=list, description="Strategies to overcome the potential challenges.")
    scientific_merit: float = Field(description="Scientific contribution value (between 0.0 and 1.0).")
    innovation_level: float = Field(description="Level of innovation and novelty (between 0.0 and 1.0).")
    thought: Optional[str] = Field(description="Thought process behind developing this idea.")

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
    similar_papers: Optional[List[SimilarPaper]] = Field(default_factory=list, description="List of similar papers with comprehensive information")