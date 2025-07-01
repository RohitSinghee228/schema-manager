from pydantic import BaseModel, Field, validator
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

class FollowUpQuestion(BaseModel):
    """Schema for follow-up questions to clarify an idea."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    question: str = Field(description="The follow-up question to ask")
    answer: str = Field(description="The answer to the follow-up question")
    
class IdeaSchema(BaseModel):
    """Schema for an individual idea."""
    name: str = Field(description="The unique name for the idea.")
    title: str = Field(description="A brief title for the idea.")
    experiment: str = Field(description="Description of the experimental approach.")
    description: str = Field(description="A comprehensive description that explains the research idea in detail.")
    implementation_steps: List[str] = Field(default_factory=list, description="Detailed step-by-step implementation plan.")
    expected_outcomes: List[str] = Field(default_factory=list, description="Expected results and outcomes of the idea.")
    potential_challenges: List[str] = Field(default_factory=list, description="Potential obstacles and challenges.")
    mitigation_strategies: List[str] = Field(default_factory=list, description="Strategies to overcome the potential challenges.")
    thought: Optional[str] = Field(description="Thought process behind developing this idea.")
    # Feedback structure – each aspect (overall, novelty, feasibility) has its own
    # dictionary with a numeric score and explanatory text. Use nested dictionaries
    # in the value type annotation to correctly represent this shape.
    feedback: Dict[str, Dict[str, Union[float, str]]] = Field(
        default_factory=lambda: {
            "overall": {"score": 0.0, "text": ""},
            "novelty": {"score": 0.0, "text": ""},
            "feasibility": {"score": 0.0, "text": ""}
        },
        description="Feedback ratings (score) and accompanying text for each aspect of the idea."
    )
    # Scores and their justifications
    novelty: Dict[str, Union[float, str]] = Field(
        default_factory=lambda: {"score": 0.0, "justification": ""},
        description="Novelty rating (1-10) and justification text"
    )
    feasibility: Dict[str, Union[float, str]] = Field(
        default_factory=lambda: {"score": 0.0, "justification": ""},
        description="Feasibility rating (1-10) and justification text"
    )
    impact: Dict[str, Union[float, str]] = Field(
        default_factory=lambda: {"score": 0.0, "justification": ""},
        description="Impact rating (1-10) and justification text"
    )
    acceptance_probability: Dict[str, Union[float, str]] = Field(
        default_factory=lambda: {"score": 0.0, "justification": ""},
        description="Acceptance probability rating (1-10) and justification text"
    )
    # Ratings
    interestingness: float = Field(description="How interesting the idea is.")
    scientific_merit: float = Field(description="Scientific contribution value (between 0.0 and 1.0).")
    innovation_level: float = Field(description="Level of innovation and novelty (between 0.0 and 1.0).")
    # Papers
    similar_papers: List[SimilarPaper] = Field(default_factory=list, description="List of similar papers.")
    # Reflection rounds
    reflection_rounds: List[Dict[str, Union[float, str]]] = Field(
        default_factory=list,
        description="List of reflection rounds with round number and the idea after the reflection"
    )
    # Validators
    @validator('scientific_merit', 'innovation_level')
    def check_score_range(cls, v):
        """Validate that scores are within the 0-1 range."""
        if v < 0.0 or v > 1.0:
            return max(0.0, min(v, 1.0))  # Clamp between 0 and 1
        return v



class IdeaTask(BaseModel):
    """Unified schema for idea generation tasks and responses."""
    # Core identifiers
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), description="Unique identifier for the task")
    task_id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Task identifier")
    user_id: str = Field(default="unknown", description="User identifier")
    
    # Task information
    task_description: str = Field(description="Description of the task")
    code: Optional[str] = Field(default="", description="Related code if applicable")
    num_ideas: Optional[int] = Field(default=1, description="Number of ideas to generate")
    num_reflections: Optional[int] = Field(default=2, description="Number of reflection rounds")
    
    # Status and content
    status: Optional[str] = Field(description="Current status of the task")
    thought: Optional[str] = Field(default=None, description="Thought process")
    ideas: Optional[List[Dict]] = Field(default_factory=list, description="Generated ideas")
    prev_ideas: Optional[List[Dict]] = Field(default_factory=list, description="Previous ideas")
    seed_ideas: Optional[List[Dict]] = Field(default_factory=list, description="Seed ideas")
    
    # System information
    system_prompt: Optional[str] = Field(default="", description="System prompt used")
    error: Optional[str] = Field(default=None, description="Error message if any")
    
    # Metadata
    tags: Optional[List[str]] = Field(default_factory=list, description="Tags associated with the task")
    metadata: Optional[dict] = Field(default_factory=dict, description="Additional metadata")
    created_at: Optional[datetime] = Field(default_factory=datetime.now, description="Creation timestamp")
    updated_at: Optional[datetime] = Field(default_factory=datetime.now, description="Last update timestamp")
    is_public: Optional[bool] = Field(default=False, description="Whether the task is public")
    
    # Related information
    similar_papers: Optional[List[SimilarPaper]] = Field(default_factory=list, description="List of similar papers")
    follow_up_questions: Optional[List[FollowUpQuestion]] = Field(default_factory=list, description="Follow-up questions")
    
    reflection_rounds: Optional[int] = Field(default=None, description="Number of reflection rounds completed")