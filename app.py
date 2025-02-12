import streamlit as st
from together import Together
from dotenv import load_dotenv
import os 

st.set_page_config(page_title="Problem Solver", page_icon="📝", layout="wide")

load_dotenv()

client = Together(api_key=os.getenv("TOGETHER_API_KEY"))

def get_math_prompt(equation):
    return [{
        "role": "user",
        "content": f"""
                    You are an expert mathematician. Please solve the following equation: {equation}. 
                    Return the answer in pure markdown with proper formatting and steps, using LaTeX for mathematical equations.
                    
                    Use the following formatting for the answer and thought process:
                    - Enclose all equations within `$$...$$` for block equations.
                    - Enclose inline equations within `$...$` for inline equations.
                    - Return the answer in the following format in markdown, do not include anything extra:
                    <think> Your thought process </think>
                    <response> Your entire response, with proper LaTeX formatting for equations </response>
                    
                    Follow the format and respect the tags.
                    """
    }]

        
def get_code_prompt(problem):
    return [{
            "role": "user",
            "content": f"""
                        You are a skilled programmer. Please write a program that solves the following problem: {problem}. 
                        Provide the answer in the following format, do not include anything extra:
                        <think> Your thought process </think>
                        <response> Your entire response </response>
                        
                        Return the answer in markdown. Follow the format and respect the tags.
                        """
        }]

def get_complex_reasoning_prompt(problem):
    return [{
            "role": "user",
            "content": f"""
                        You are a brilliant thinker. Please solve the following problem: {problem}. 
                        Provide the answer in the following format, do not include anything extra:
                        <think> Your thought process </think>
                        <response> Your entire response </response>
                        
                        Return the answer in markdown. Follow the format and respect the tags.
                        """
        }]

def get_prompt(problem_type, problem):
    if problem_type == "Math":
        return get_math_prompt(problem)
    elif problem_type == "Code":
        return get_code_prompt(problem)
    else:
        return get_complex_reasoning_prompt(problem)
    
def get_solution(prompt):
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-R1",
        messages=prompt,
        temperature=0.3,
        stop=["< | end_of_sentence | >"]
    )
    return response.choices[0].message.content

def get_thought_response(solution):
    think = solution.split("<think>")[1].split("</think>")[0]
    response = solution.split("<response>")[1].split("</response>")[0]
    return think, response

st.title("Solve Problems using DeepSeek R1")
st.write("This application uses Together AI's Deepseek R1 API to generate solutions to problems.")

problem_type = st.selectbox("Select the type of problem", ["Complex Reasoning", "Code", "Math"])

if problem_type == "Math":
    user_input = st.text_input("Enter a mathematical equation in latex:")

    if user_input:
        try:
            st.latex(user_input)
        except Exception as e:
            st.error(f"Invalid equation: {e}")

elif problem_type == "Code":
    user_input = st.text_area("Enter a programming problem statement:")
    
else:
    user_input = st.text_area("Enter a complex reasoning problem statement:")
            
if st.button("Get Solution"):
    with st.spinner("Thinking..."):
        if not user_input:
            st.warning("Please enter a problem statement.")
            st.stop()
        
        try: 
            prompt = get_prompt(problem_type, user_input)
            solution = get_solution(prompt)
            
            think, response = get_thought_response(solution)
            
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Thought Process")
                st.markdown(think)
                
            with col2:
                st.subheader("Solution")
                st.markdown(response)
            
        except Exception as e:
            st.error(f"Failed to get solution: {e}")