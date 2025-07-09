# Health-And-Wellness-Agent-_

+ Health & Wellness Planner Agent
An AI-powered assistant for fitness goals, meal planning, and workout routines.

✨ Features
Goal Tracking: Set and analyze fitness goals (e.g., "lose 5kg in 2 months").

Meal Planning: Generate personalized 7-day meal plans based on dietary preferences.

Workout Recommendations: Get tailored workout routines (strength, cardio, etc.).

Progress Tracking: Log updates and receive motivational feedback.

Specialized Support: Handoffs to experts for injuries, nutrition, or human coaching.

Real-Time Interaction: Streamlit-powered chat interface.

🛠️ Installation
Clone the repo:

bash
git clone https://github.com/Fatima2417/Health-And-Wellness-Agent-_.git
cd health-wellness-agent
Install required packages:

bash
pip install streamlit pydantic requests
Add your OpenRouter API key to utils/openrouter_client.py:

python
self.api_key = "your_api_key_here"

🚀 Usage
Run the Streamlit app:

bash
streamlit run main.py
Quick Actions
Set Goal: Define a fitness target (e.g., "Gain 5kg muscle in 3 months").

Meal Plan: Request a diet plan (e.g., "Vegetarian meal plan for weight loss").

Workout Plan: Get exercises (e.g., "Beginner-friendly home workouts").

📂 Project Structure
text
health-wellness-agent/
├── main.py               # Streamlit frontend
├── agent.py              # Main agent logic
├── context.py            # User session management
├── guardrails.py         # Input/output validation
├── tools/                # Functional tools
│   ├── goal_analyzer.py
│   ├── meal_planner.py
│   ├── workout_recommender.py
│   ├── tracker.py
│   └── scheduler.py
├── agents/               # Specialized agents
│   ├── escalation_agent.py
│   ├── nutrition_expert_agent.py
│   └── injury_support_agent.py
└── utils/                # Helper modules
    ├── streaming.py
    └── openrouter_client.py
🔧 Dependencies
Python 3.8+

streamlit (for UI)

pydantic (context modeling)

requests (API calls)

📜 License
MIT
