# Schema Manager

The Schema Manager is a central repository for Pydantic data schemas used across the Ideaverse microservices architecture. It provides a single source of truth for data structures, ensuring consistency across different services.

## Available Schemas

### idea.py
- `SimilarPaper`: Schema for similar paper information
- `FollowUpQuestion`: Schema for follow-up questions to clarify an idea
- `FollowUpAnswer`: Schema for answers to follow-up questions
- `IdeaGenerationTask`: Schema for idea generation task requests
- `IdeaResponse`: Schema for idea generation responses
- `IdeaPromptSchema`: Schema for idea prompt formatting
- `IdeaTasksResponse`: Schema for idea task listing responses

### user.py
- `UserBase`: Base schema for user data
- `UserCreate`: Schema for creating a new user
- `UserUpdate`: Schema for updating user information
- `UserPasswordUpdate`: Schema for updating a user's password
- `UserPreferencesUpdate`: Schema for updating user preferences
- `UserResponse`: Schema for user response data
- `UserLogin`: Schema for user login
- `User`: Simplified user schema

### code.py
- Contains schemas for code-related operations

### paper.py
- Contains schemas for academic paper operations

### project.py
- Contains schemas for project management

### common.py
- Contains common utility schemas

### credit.py
- Contains schemas for credit management

## Service Dependencies

This section documents which services use which schemas to help with future updates and maintenance.

### Idea Generation Service
- `schema_manager.idea.SimilarPaper`
- `schema_manager.idea.IdeaGenerationTask`
- `schema_manager.idea.IdeaResponse`
- `schema_manager.idea.IdeaPromptSchema`
- `schema_manager.idea.FollowUpQuestion`

### Backend Server
- `schema_manager.idea.IdeaGenerationTask`
- `schema_manager.idea.IdeaResponse`
- `schema_manager.idea.IdeaTasksResponse`
- `schema_manager.idea.FollowUpQuestion`
- `schema_manager.idea.FollowUpAnswer`

### DB Manager
- `schema_manager.idea.IdeaResponse`

## Adding New Schemas

When adding a new schema:
1. Place it in the appropriate file based on its domain
2. Update this README to document its usage
3. Import it in the `__init__.py` file to make it accessible through the package

## Modifying Existing Schemas

When modifying an existing schema:
1. Refer to the Service Dependencies section to identify affected services
2. Ensure backward compatibility when possible
3. If breaking changes are necessary, coordinate updates across dependent services
4. Update this README if the schema's usage changes