from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Generative AI with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Generative Model
try:
    model = genai.GenerativeModel("gemini-pro")  # Use the correct model name
except Exception as e:
    st.error(f"Error initializing the model: {e}")
    st.stop()

# Function to get AI response
def my_output(query):
    try:
        response = model.generate_content(query)
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI Development
st.set_page_config(page_title="SMART_BOT", layout="centered")
st.title("🤖 SMART_BOT")
st.markdown("Ask your queries and get instant responses powered by Google Generative AI!")

# Initialize session state for maintaining chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User Input Section
with st.form("query_form", clear_on_submit=True):
    user_input = st.text_input("Type your query:", key="input")
    submit = st.form_submit_button("Ask")

# Process the query and display the response
if submit:
    if user_input.strip():
        # Add user input to the chat history
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Get AI response
        response = my_output(user_input)
        st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        st.warning("Please enter a valid query.")

# Display Chat History
st.subheader("Chat History")
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**🧑 You:** {message['content']}")
    else:
        st.markdown(f"**🤖 SMART_BOT:** {message['content']}")

# Footer
st.markdown("---")
st.caption("Powered by Google Generative AI.")
