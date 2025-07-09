from context import UserSessionContext
from guardrails import InputGuardrails

class GoalAnalyzerTool:
    def __init__(self, client):
        self.client = client
        self.guardrails = InputGuardrails()
    
    async def execute(self, user_input: str, context: UserSessionContext) -> str:
        goal_data = self.guardrails.validate_goal_input(user_input)
        
        if goal_data.get("needs_clarification"):
            return await self._request_clarification(user_input, context)
        
        await self._analyze_goal(goal_data, context)
        return f"🎯 **Goal Set**: {goal_data['goal_type'].title()} goal created successfully!"
    
    async def _request_clarification(self, user_input: str, context: UserSessionContext) -> str:
        system_prompt = "Help clarify fitness goals. Ask specific questions about target, timeline, and preferences."
        return await self.client.chat_completion(system_prompt, f"Clarify this goal: {user_input}")
    
    async def _analyze_goal(self, goal_data, context: UserSessionContext):
        context.update_goal(goal_data)