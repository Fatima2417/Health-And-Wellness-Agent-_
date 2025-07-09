from context import UserSessionContext

class ProgressTrackerTool:
    def __init__(self, client):
        self.client = client
    
    async def execute(self, user_input: str, context: UserSessionContext) -> str:
        analysis = await self._analyze_progress(user_input, context)
        context.add_progress_log(user_input)
        return self._generate_feedback(analysis, context)
    
    async def _analyze_progress(self, user_input: str, context: UserSessionContext):
        system_prompt = """Analyze user progress updates and provide motivational feedback.
        Look for patterns, celebrate achievements, and suggest improvements."""
        
        progress_context = f"""
        Progress update: {user_input}
        User context: {context.to_context_string()}
        
        Analyze this progress update and provide encouraging, actionable feedback.
        """
        
        return await self.client.chat_completion(system_prompt, progress_context)
    
    def _calculate_goal_progress(self, update: str, context: UserSessionContext) -> str:
        if context.goal and "quantity" in context.goal:
            return "Progress calculation based on goal metrics"
        return "Keep tracking your progress!"
    
    def _generate_feedback(self, analysis, context: UserSessionContext) -> str:
        return f"📈 **Progress Analysis**\n\n{analysis}"