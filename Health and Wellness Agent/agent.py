from context import UserSessionContext
from utils.streaming import OpenRouterClient
from tools.goal_analyzer import GoalAnalyzerTool
from tools.meal_planner import MealPlannerTool
from tools.workout_recommender import WorkoutRecommenderTool
from tools.scheduler import CheckinSchedulerTool
from tools.tracker import ProgressTrackerTool
from agents.escalation_agent import EscalationAgent
from agents.nutrition_expert_agent import NutritionExpertAgent
from agents.injury_support_agent import InjurySupportAgent
from guardrails import InputGuardrails

class HealthWellnessAgent:
    def __init__(self):
        self.client = OpenRouterClient()
        self.tools = {
            "goal_analyzer": GoalAnalyzerTool(self.client),
            "meal_planner": MealPlannerTool(self.client),
            "workout_recommender": WorkoutRecommenderTool(self.client),
            "checkin_scheduler": CheckinSchedulerTool(self.client),
            "progress_tracker": ProgressTrackerTool(self.client)
        }
        self.agents = {
            "escalation": EscalationAgent(self.client),
            "nutrition_expert": NutritionExpertAgent(self.client),
            "injury_support": InjurySupportAgent(self.client)
        }
        self.guardrails = InputGuardrails()

    async def process_message(self, message: str, context: UserSessionContext) -> str:
        # for the input guardrail
        message = self.guardrails.sanitize_input(message)
        
        # checking for handoff conditions
        handoff_agent = self._check_handoff_conditions(message, context)
        if handoff_agent:
            context.handoff_logs.append(f"Handed off to {handoff_agent}")
            return await self.agents[handoff_agent].handle_request(message, context)
        
        # tool selec
        tool_name = self._determine_tool(message, context)
        if tool_name:
            return await self.tools[tool_name].execute(message, context)
        
        return await self._general_response(message, context)

    def _check_handoff_conditions(self, message: str, context: UserSessionContext) -> str:
        message_lower = message.lower()
        
        if any(word in message_lower for word in ["human", "trainer", "coach"]):
            return "escalation"
        elif any(word in message_lower for word in ["diabetes", "allergy", "medical"]):
            return "nutrition_expert"
        elif any(word in message_lower for word in ["injury", "pain", "hurt"]):
            return "injury_support"
        
        return None

    def _determine_tool(self, message: str, context: UserSessionContext) -> str:
        message_lower = message.lower()
        
        if any(word in message_lower for word in ["goal", "want to", "target"]) and not context.goal:
            return "goal_analyzer"
        elif any(word in message_lower for word in ["meal", "food", "diet"]):
            return "meal_planner"
        elif any(word in message_lower for word in ["workout", "exercise", "fitness"]):
            return "workout_recommender"
        elif any(word in message_lower for word in ["progress", "update", "achieved"]):
            return "progress_tracker"
        elif any(word in message_lower for word in ["schedule", "reminder", "check-in"]):
            return "checkin_scheduler"
        
        return None

    async def _general_response(self, message: str, context: UserSessionContext) -> str:
        system_prompt = f"You are a helpful Health & Wellness Assistant. User context: {context.to_context_string()}"
        return await self.client.chat_completion(system_prompt, message)