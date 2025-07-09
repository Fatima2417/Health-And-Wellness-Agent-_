import streamlit as st
import asyncio
from agent import HealthWellnessAgent
from context import UserSessionContext

def main():
    st.title("+ Health & Wellness Planner Agent")
    st.write("It is health that is real wealth and not pieces of gold and silver")
    
    # sessin state initializing
    if "context" not in st.session_state:
        st.session_state.context = UserSessionContext(name="User", uid=12345)
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "agent" not in st.session_state:
        st.session_state.agent = HealthWellnessAgent()
    
    # slidebar sec
    with st.sidebar:
        st.header("📊 Profile")
        ctx = st.session_state.context
        if ctx.goal:
            st.subheader("🎯 Goal")
            st.json(ctx.goal)
        if ctx.progress_logs:
            st.subheader("📈 Progress")
            for log in ctx.progress_logs[-3:]:
                st.write(f"• {log['date']}: {log['update'][:50]}...")
    
    # for chatting
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
    
    if prompt := st.chat_input("How can I help with your wellness goals?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        
        with st.chat_message("assistant"):
            with st.spinner("Thinking...."):
                response = asyncio.run(st.session_state.agent.process_message(prompt, st.session_state.context))
                st.write(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
    
    # for quick Actions
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🎯 Set Goal"):
            _quick_action("I want to set a fitness goal")
    with col2:
        if st.button("🥗 Meal Plan"):
            _quick_action("Create a meal plan")
    with col3:
        if st.button("💪 Workout"):
            _quick_action("Creating a workout plan")

def _quick_action(prompt):
    response = asyncio.run(st.session_state.agent.process_message(prompt, st.session_state.context))
    st.session_state.messages.extend([
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": response}
    ])
    st.rerun()

if __name__ == "__main__":
    main()
    
##### Created by Fatima #####