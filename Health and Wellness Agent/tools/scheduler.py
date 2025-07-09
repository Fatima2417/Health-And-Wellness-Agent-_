from context import UserSessionContext

class CheckinSchedulerTool:
    def __init__(self, client):
        self.client = client
    
    async def execute(self, user_input: str, context: UserSessionContext) -> str:
        schedule = await self._create_schedule(user_input, context)
        return self._format_schedule_response(schedule, context)
    
    async def _create_schedule(self, user_input: str, context: UserSessionContext):
        system_prompt = """Create a check-in schedule for tracking wellness progress.
        Include specific dates, times, and what to track (weight, measurements, mood, etc.)."""
        
        schedule_context = f"""
        Request: {user_input}
        User context: {context.to_context_string()}
        
        Create a realistic check-in schedule with reminders and tracking points.
        """
        
        return await self.client.chat_completion(system_prompt, schedule_context)
    
    def _format_schedule_response(self, schedule, context: UserSessionContext) -> str:
        return f"📅 **Check-in Schedule Created**\n\n{schedule}"