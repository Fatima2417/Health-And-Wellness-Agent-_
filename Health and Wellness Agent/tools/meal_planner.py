from context import UserSessionContext

class MealPlannerTool:
    def __init__(self, client):
        self.client = client
    
    async def execute(self, user_input: str, context: UserSessionContext) -> str:
        meal_plan = await self._generate_meal_plan(user_input, context)
        context.update_meal_plan([meal_plan])
        return self._format_meal_plan_response(meal_plan, context)
    
    async def _generate_meal_plan(self, user_input: str, context: UserSessionContext):
        system_prompt = """Create a 7-day meal plan based on user preferences and goals.
        Include breakfast, lunch, dinner, and snacks. Consider dietary restrictions."""
        
        meal_context = f"""
        Request: {user_input}
        User context: {context.to_context_string()}
        
        Create a balanced weekly meal plan with specific meals and portion guidance
        """
        
        return await self.client.chat_completion(system_prompt, meal_context)
    
    def _format_meal_plan_response(self, meal_plan, context: UserSessionContext) -> str:
        return f"🥗 **7-Day Meal Plan Created**\n\n{meal_plan}"