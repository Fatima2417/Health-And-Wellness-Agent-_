from context import UserSessionContext

class EscalationAgent:
    def __init__(self, client):
        self.client = client
    
    async def handle_request(self, user_input: str, context: UserSessionContext) -> str:
        system_prompt = """You are an escalation agent for health and wellness.
        When users request human coaches or trainers, explain that this is an AI system
        and suggest connecting with qualified professionals in their area and also ask if i can also help you."""
        
        escalation_context = f"""
        User request: {user_input}
        Context: {context.to_context_string()}
        
        Provide guidance on finding qualified health professionals and explain
        the limitations of AI health advice and end with a beautiful quote related to health.
        """
        
        response = await self.client.chat_completion(system_prompt, escalation_context)
        return f"🚨 **Escalation**: {response}"