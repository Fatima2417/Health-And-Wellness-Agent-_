from context import UserSessionContext

class NutritionExpertAgent:
    def __init__(self, client):
        self.client = client
    
    async def handle_request(self, user_input: str, context: UserSessionContext) -> str:
        system_prompt = """You are a specialized nutrition expert agent.
        Handle complex dietary needs, medical conditions, and allergies.
        Always recommend consulting healthcare providers for medical conditions."""
        
        nutrition_context = f"""
        User request: {user_input}
        Context: {context.to_context_string()}
        
        Provide specialized nutrition advice while emphasizing the importance
        of professional medical consultation for health conditions and types.
        """
        
        response = await self.client.chat_completion(system_prompt, nutrition_context)
        context.update_diet_preferences(user_input)
        return f"🥗 **Nutrition Expert**: {response}"