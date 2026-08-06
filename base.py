import uuid
from dataclasses import dataclass, field
from typing import Any, Dict, Optional

@dataclass
class AgentResponse:
    agent: str
    text: str
    structured: Optional[Dict[str, Any]] = None
    confidence: Optional[int] = None
    disclaimer: str = "AI-generated decision support. Verify high-impact actions with an authorized extension officer."
    meta: Dict[str, Any] = field(default_factory=dict)
    def to_dict(self):
        return {"agent":self.agent,"text":self.text,"structured":self.structured,"confidence":self.confidence,"disclaimer":self.disclaimer,**self.meta}

class BaseAgent:
    name="base"; display_name="Base Agent"; description=""; icon="cpu"; role_required=None
    def __init__(self, api_key=""): self.api_key=api_key
    async def run(self,payload,**kwargs):
        return AgentResponse(self.name,f"{self.display_name} is configured but no production provider adapter is connected.",{"status":"provider_not_connected","data_gaps":["AI provider adapter"],"review_required":True},0,{"run_id":str(uuid.uuid4())})
    @classmethod
    def metadata(cls):
        return {"name":cls.name,"display_name":cls.display_name,"description":cls.description,"icon":cls.icon,"role_required":cls.role_required}
