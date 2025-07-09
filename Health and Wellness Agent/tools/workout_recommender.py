from context import UserSessionContext

class WorkoutRecommenderTool:
    def __init__(self, client):
        self.client = client
    
    async def execute(self, user_input: str, context: UserSessionContext) -> str:
        workout_plan = await self._generate_workout_plan(user_input, context)
        context.update_workout_plan({"plan": workout_plan})
        return self._format_workout_response(workout_plan, context)
    
    async def _generate_workout_plan(self, user_input: str, context: UserSessionContext):
        system_prompt = """Create a weekly workout plan based on user goals and fitness level.
        Include specific exercises, sets, reps, and rest periods."""
        
        workout_context = f"""
        Request: {user_input}
        User context: {context.to_context_string()}
        
        Design a balanced weekly workout routine with progressive difficulty.
        """
        
        return await self.client.chat_completion(system_prompt, workout_context)
    
    def _format_workout_response(self, workout_plan, context: UserSessionContext) -> str:
        return f"💪 **Weekly Workout Plan Created**\n\n{workout_plan}"