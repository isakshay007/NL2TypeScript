import streamlit as st
from lyzr_automata.ai_models.openai import OpenAIModel
from lyzr_automata import Agent, Task
from lyzr_automata.pipelines.linear_sync_pipeline import LinearSyncPipeline
from PIL import Image
from lyzr_automata.tasks.task_literals import InputType, OutputType
import os

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = st.secrets["apikey"]

st.markdown(
    """
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

image = Image.open("./logo/lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("NL2TypeScript🧑‍💻")
st.markdown("Welcome to NL2TypeScript! Translate natural language prompts into accurate TypeScript queries effortlessly. ")
input = st.text_input("Please enter your natural language prompt:",placeholder=f"""Type here""")

open_ai_text_completion_model = OpenAIModel(
    api_key=st.secrets["apikey"],
    parameters={
        "model": "gpt-4-turbo-preview",
        "temperature": 0.2,
        "max_tokens": 1500,
    },
)


def generation(input):
    generator_agent = Agent(
        role=" Expert TYPESCRIPT DEVELOPER",
        prompt_persona=f" Your task is to TRANSLATE natural language prompts into EFFICIENT and CONTEXTUALLY ACCURATE TypeScript code.")
    prompt = f"""
You are an Expert TYPESCRIPT DEVELOPER. Your task is to TRANSLATE natural language prompts into EFFICIENT and CONTEXTUALLY ACCURATE TypeScript code.
Here's your step-by-step guide:

1. Analyze the user's natural language prompt CAREFULLY to fully understand the functionality they desire.

2. CONVERT the natural language instructions into precise TypeScript syntax, focusing on CLARITY and PERFORMANCE. Ensure it aligns with the prompt's context.

3. VERIFY that all VARIABLES, FUNCTIONS, and INTERFACES are named appropriately to match their purpose as described in the prompt.

4. TEST the TypeScript code to CONFIRM that it performs as expected and meets the user's needs accurately.

5. REVIEW your work to ensure there is a DIRECT CORRELATION between the entered prompt and the generated TypeScript code.

6.DISPLAY the generated TypeScript Code after completing all the above steps.

You MUST ensure that every piece of TypeScript you generate is a DIRECT REFLECTION of what the user intends, leaving no room for misinterpretation or errors.

 """

    generator_agent_task = Task(
        name="Generation",
        model=open_ai_text_completion_model,
        agent=generator_agent,
        instructions=prompt,
        default_input=input,
        output_type=OutputType.TEXT,
        input_type=InputType.TEXT,
    ).execute()

    return generator_agent_task 
   
if st.button("Convert"):
    solution = generation(input)
    st.markdown(solution)

with st.expander("ℹ️ - About this App"):
    st.markdown("""
    This app uses Lyzr Automata Agent . For any inquiries or issues, please contact Lyzr.

    """)
    st.link_button("Lyzr", url='https://www.lyzr.ai/', use_container_width=True)
    st.link_button("Book a Demo", url='https://www.lyzr.ai/book-demo/', use_container_width=True)
    st.link_button("Discord", url='https://discord.gg/nm7zSyEFA2', use_container_width=True)
    st.link_button("Slack",
                   url='https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw',
                   use_container_width=True)