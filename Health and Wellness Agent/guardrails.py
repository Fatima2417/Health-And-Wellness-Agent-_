import re
from typing import Dict, Any
import json

class InputGuardrails:
    def validate_goal_input(self, user_input: str) -> Dict[str, Any]:
        patterns = [
            r"(\d+(?:\.\d+)?)\s*(\w+)\s+(?:in|within|over)\s+(\d+)\s*(\w+)"
        ]
        
        for pattern in patterns:
            match = re.search(pattern, user_input.lower())
            if match:
                groups = match.groups()
                return {
                    "quantity": float(groups[0]),
                    "metric": groups[1],
                    "duration": f"{groups[2]} {groups[3]}",
                    "goal_type": self._determine_goal_type(user_input)
                }
        
        return {"raw_input": user_input, "needs_clarification": True}
    
    
    def _determine_goal_type(self, input_text: str) -> str:
        input_lower = input_text.lower()
        
        if any(word in input_lower for word in ["lose", "weight loss", "cut"]):
            return "weight_loss"
        elif any(word in input_lower for word in ["gain", "build", "muscle"]):
            return "muscle_gain"
        elif any(word in input_lower for word in ["fitness", "endurance", "cardio"]):
            return "fitness"
        else:
            return "general"
    
    def sanitize_input(self, user_input: str) -> str:
        sanitized = re.sub(r'[<>"\']', '', user_input)
        sanitized = sanitized[:500]
        sanitized = sanitized.strip()
        return sanitized


class OutputGuardrails:
    def validate_meal_plan(self, meal_plan: Any) -> Dict[str, Any]:
        if isinstance(meal_plan, str):
            try:
                meal_plan = json.loads(meal_plan)
            except json.JSONDecodeError:
                return {"valid": False, "error": "Invalid JSON format"}
        
        return {"valid": True, "data": meal_plan}
    
    
    def validate_workout_plan(self, workout_plan: Any) -> Dict[str, Any]:
        if isinstance(workout_plan, str):
            try:
                workout_plan = json.loads(workout_plan)
            except json.JSONDecodeError:
                return {"valid": False, "error": "Invalid JSON format"}
        
        return {"valid": True, "data": workout_plan}
    
    
    def format_response(self, response: str) -> str:
        if len(response) > 1000:
            response = response[:997] + "..."
        
        return response.strip()
