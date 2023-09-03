from typing import List, Optional
from pydantic import BaseModel, Field, constr

class ModelParameters(BaseModel):
    model_name: str
    temperature: float
    max_len: int

class PromptParameters(BaseModel):
    TARGET_LANGUAGE: str
    USER_INPUT: constr(max_length=2000)