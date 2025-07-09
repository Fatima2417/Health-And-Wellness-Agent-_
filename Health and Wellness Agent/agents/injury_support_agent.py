from context import UserSessionContext

class InjurySupportAgent:
    def __init__(self, client):
        self.client = client
    
    async def handle_request(self, user_input: str, context: UserSessionContext) -> str:
        system_prompt = """You are an injury support agent for fitness planning.
        Provide safe exercise modifications for injuries and always recommend
        consulting healthcare providers for injury assessment and treatment."""
        
        injury_context = f"""
        User request: {user_input}
        Context: {context.to_context_string()}
        
        Provide safe exercise alternatives and modifications while emphasizing
        the importance of professional medical evaluation for injuries and end with the powerful personalize quote according to the situation  .
        """
        
        response = await self.client.chat_completion(system_prompt, injury_context)
        context.add_injury_note(user_input)
        return f"🩹 **Injury Support**: {response}"