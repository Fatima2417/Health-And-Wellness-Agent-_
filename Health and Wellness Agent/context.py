from pydantic import BaseModel
from typing import Optional, List, Dict
from datetime import datetime

class UserSessionContext(BaseModel):
    name: str
    uid: int
    goal: Optional[dict] = None
    diet_preferences: Optional[str] = None
    workout_plan: Optional[dict] = None
    meal_plan: Optional[List[str]] = None
    injury_notes: Optional[str] = None
    handoff_logs: List[str] = []
    progress_logs: List[Dict[str, str]] = []
    
    
    def update_goal(self, goal_data: dict):
        self.goal = goal_data
    
    def update_diet_preferences(self, preferences: str):
        self.diet_preferences = preferences
    
    def update_workout_plan(self, plan: dict):
        self.workout_plan = plan
    
    def update_meal_plan(self, plan: List[str]):
        self.meal_plan = plan
    
    def add_injury_note(self, note: str):
        self.injury_notes = note
    
    def add_progress_log(self, update: str, date: str = None):
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        
        self.progress_logs.append({
            "date": date,
            "update": update
        
        })
    
    
    def to_context_string(self) -> str:
        context_info = []
        
        if self.goal:
            context_info.append(f"Goal: {self.goal}")
        if self.diet_preferences:
            context_info.append(f"Diet: {self.diet_preferences}")
        if self.injury_notes:
            context_info.append(f"Injuries: {self.injury_notes}")
        if self.progress_logs:
            context_info.append(f"Recent progress: {self.progress_logs[-3:]}")
        
        return " | ".join(context_info) if context_info else "No previous context"
