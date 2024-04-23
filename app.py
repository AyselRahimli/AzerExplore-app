import streamlit as st
from transformers import Conversation, ConversationPipeline

pipe = ConversationPipeline("microsoft/DialoGPT-medium")

def generate_activity_plan(city, days):
    if city.lower() == "shaki":
        if days == 1:
            messages = [
                {"role": "user", "content": "I want to spend 1 day in Shaki, Azerbaijan."},
                {"role": "Tourist guide", "content": "Provide 3 options for different activities in popular places of the city for tourists."},
            ]
        elif days == 3:
            messages = [
                {"role": "user", "content": "I want to spend 3 days in Shaki, Azerbaijan."},
                {"role": "Tourist guide", "content": "Provide 3 options for different activities in popular places of the city for tourists."},
            ]
        elif days == 7:
            messages = [
                {"role": "user", "content": "I want to spend a week in Shaki, Azerbaijan."},
                {"role": "Tourist guide", "content": "Provide 3 options for different activities in popular places of the city for tourists."},
            ]
        else:
            return "Sorry, I can only generate activity plans for 1, 3, or 7 days."
    elif city.lower() == "baku":
        if days == 1:
            messages = [
                {"role": "user", "content": "I want to spend 1 day in Baku, Azerbaijan."},
                {"role": "Tourist guide", "content": "Provide 3 options for different activities in popular places of the city for tourists."},
            ]
        elif days == 3:
            messages = [
                {"role": "user", "content": "I want to spend 3 days in Baku, Azerbaijan."},
                {"role": "Tourist guide", "content": "Provide 3 options for different activities in popular places of the city for tourists."},
            ]
        elif days == 7:
            messages = [
                {"role": "user", "content": "I want to spend a week in Baku, Azerbaijan."},
                {"role": "Tourist guide", "content": "Provide 3 options for different activities in popular places of the city for tourists."},
            ]
        else:
            return "Sorry, I can only generate activity plans for 1, 3, or 7 days."
    elif city.lower() == "guba":
      if days == 1:
            messages = [
                 {"role": "user", "content": "I want to spend 1 day in Guba, Azerbaijan."},
                 {"role": "Tourist guide", "content": "Provide 3 options for different activities in popular places of the city for tourists."},
            ]
      elif days == 3:
              messages = [
                  {"role": "user", "content": "I want to spend 3 days in Guba, Azerbaijan."},
                  {"role": "Tourist guide", "content": "Provide 3 options for different activities in popular places of the city for tourists."},
              ]
      elif days == 7:
              messages = [
                  {"role": "user", "content": "I want to spend a week in Guba, Azerbaijan."},
                  {"role": "Tourist guide", "content": "Provide 3 options for different activities in popular places of the city for tourists."},
              ]
      else:
              return "Sorry, I can only generate activity plans for 1, 3, or 7 days."
         
    elif city.lower() == "karabakh":
      if days == 1:
            messages = [
                 {"role": "user", "content": "I want to spend 1 day in Susha, Azerbaijan."},
                 {"role": "Tourist guide", "content": "Provide 3 options for different activities in popular places of the city for tourists."},
            ]
      elif days == 3:
              messages = [
                  {"role": "user", "content": "I want to spend 3 days in Susha, Azerbaijan."},
                  {"role": "Tourist guide", "content": "Provide 3 options for different activities in popular places of the city for tourists."},
              ]
      elif days == 7:
              messages = [
                  {"role": "user", "content": "I want to spend a week in Susha, Azerbaijan."},
                  {"role": "Tourist guide", "content": "Provide 3 options for different activities in popular places of the city for tourists."},
              ]
      else:
              return "Sorry, I can only generate activity plans for 1, 3, or 7 days."
                
    elif city.lower() == "nakchivan":
      if days == 1:
            messages = [
                 {"role": "user", "content": "I want to spend 1 day in Nakchivan, Azerbaijan."},
                 {"role": "Tourist guide", "content": "Provide 3 options for different activities in popular places of the city for tourists."},
            ]
      elif days == 3:
              messages = [
                  {"role": "user", "content": "I want to spend 3 days in Nakchivan, Azerbaijan."},
                  {"role": "Tourist guide", "content": "Provide 3 options for different activities in popular places of the city for tourists."},
              ]
      elif days == 7:
              messages = [
                  {"role": "user", "content": "I want to spend a week in Nakchivan, Azerbaijan."},
                  {"role": "Tourist guide", "content": "Provide 3 options for different activities in popular places of the city for tourists."},
              ]
      else:
              return "Sorry, I can only generate activity plans for 1, 3, or 7 days."
    else:
        return "Sorry, I can only generate activity plans for Shaki, Baku, Guba, Karabakh, or Nakchivan."


    conv = Conversation(messages=messages)
    conv = pipe(conv)

  
    response = conv.generated_responses[-1]["generated_text"]
    return response

# Define the application title and layout
st.title("Azerbaijan Activity Planner")
st.write("This application helps you plan your activities in different cities of Azerbaijan.")

# Create a menu bar for navigation
menu = ["Home", "Baku", "Shaki", "Guba", "Karabakh", "Nakchivan"]
choice = st.sidebar.selectbox("Select City", menu)

# Display different pages based on the user's choice
if choice == "Home":
    st.write("# Welcome to Azerbaijan!")
    st.image("azerbaijan.jpg", use_column_width=True)
else:
    # Create a form to collect user input
    with st.form("user_input"):
        # Get the number of days the user wants to spend
        days = st.selectbox(f"How many days do you want to spend in {choice}?", [1, 3, 7])

        # Submit button
        submitted = st.form_submit_button("Generate Activity Plan")

    # Generate the activity plan based on user input
    if submitted:
        activity_plan = generate_activity_plan(choice, days)
        st.write(activity_plan)
