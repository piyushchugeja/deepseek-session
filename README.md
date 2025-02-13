# DeepSeek Model Exploration and Streamlit App

## Overview
This repository provides a structured approach to exploring and utilizing the DeepSeek-R1-Distill-Qwen-1.5B model for text generation, problem-solving, and reasoning tasks. It includes a Jupyter Notebook for in-depth experimentation and a Streamlit app that offers a user-friendly interface to interact with the model.

This session was conducted by **Attreyee Mukherjee** and **Piyush Chugeja**, on behalf of **CodeCell**, on **February 13, 2025**, from **11 AM to 1 PM**.

## Prerequisites
Before running the notebook or Streamlit app, ensure you meet the following requirements:

- **Access to DeepSeek on Hugging Face:** Make sure you have permission to use the `deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B` model from Hugging Face.
- **Together AI API Key:** If using the Streamlit app, you need an API key from Together AI to interact with the model.
- **Python Environment:** Ensure you have Python installed (preferably Python 3.8+).
- **Required Libraries:** Install necessary dependencies such as `transformers`, `torch`, `streamlit`, and `python-dotenv`.

## Notebook Details
The Jupyter Notebook demonstrates how to:

- Load the DeepSeek model and tokenizer using the Hugging Face Transformers library.
- Generate structured responses with thought reasoning and markdown-formatted output.
- Use structured prompts for solving mathematical problems, coding tasks, and complex reasoning challenges.

## Streamlit App
The Streamlit application provides a simplified way to interact with the model:

- Users can select from different problem types: **Math, Code, or Complex Reasoning**.
- The app formats responses with structured `<think>` and `<response>` tags.
- Responses include markdown and LaTeX formatting for mathematical equations.
- The app fetches solutions from the Together AI API and presents structured answers.

## Running the Streamlit App
To launch the app, simply run the Streamlit script and enter your problem statement. The model will process your input and generate a well-structured response.

## Conclusion
This repository serves as a guide for exploring the DeepSeek-R1-Distill-Qwen-1.5B model in both research and practical applications. Whether through the Jupyter Notebook or the interactive Streamlit app, users can leverage DeepSeek’s capabilities for structured reasoning and problem-solving.