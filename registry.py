from .base import BaseAgent
class CropDoctorAgent(BaseAgent):
    name="crop_doctor"; display_name="Crop Intelligence"; description="Provisional crop-health analysis with escalation."; icon="camera"
class VoiceAgronomistAgent(BaseAgent):
    name="voice_agronomist"; display_name="Voice Agronomist"; description="Multilingual agricultural Q&A."; icon="mic"
class PostHarvestAgent(BaseAgent):
    name="post_harvest"; display_name="Post-Harvest Predictor"; description="Storage and spoilage-risk ranges."; icon="package"
class MarketIntelAgent(BaseAgent):
    name="market_intel"; display_name="Market Intelligence"; description="Verified-source market analysis without fabricated prices."; icon="trending-up"
class EscalationReviewerAgent(BaseAgent):
    name="escalation_reviewer"; display_name="Escalation Reviewer"; description="Officer-facing second-opinion support."; icon="shield"; role_required="officer"
REGISTRY={c.name:c for c in [CropDoctorAgent,VoiceAgronomistAgent,PostHarvestAgent,MarketIntelAgent,EscalationReviewerAgent]}
def get_agent_class(name):
    if name not in REGISTRY: raise KeyError(name)
    return REGISTRY[name]
