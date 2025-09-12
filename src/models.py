from typing import Optional, List
from pydantic import BaseModel, Field

class ModelScore(BaseModel):
    model_url: str
    size: float = Field(..., ge=0, le=1)
    license: float = Field(..., ge=0, le=1)
    ramp_up: float = Field(..., ge=0, le=1)
    bus_factor: float = Field(..., ge=0, le=1)
    dataset_code_avail: float = Field(..., ge=0, le=1)
    dataset_quality: float = Field(..., ge=0, le=1)
    code_quality: float = Field(..., ge=0, le=1)
    perf_claims: float = Field(..., ge=0, le=1)
    net_score: float = Field(..., ge=0, le=1)
    latencies_ms: dict
    linked_dataset: Optional[str]
    linked_code: Optional[str]
