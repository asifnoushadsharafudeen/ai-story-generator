# ----------------------------
# 🚀 PHASE 2: FastAPI backend
# ----------------------------

# from fastapi import FastAPI
# from pydantic import BaseModel
# from generator import generate_story

# app = FastAPI()

# class PromptRequest(BaseModel):
#     prompt: str

# @app.post("/generate")
# def generate(req: PromptRequest):
#     story = generate_story(req.prompt)
#     return {"story": story}


# ----------------------------
# 🎨 PHASE 3: Gradio Interface
# ----------------------------

import gradio as gr
from generator import generate_story

def story_interface(prompt, context=""):
    final_prompt = context if context.strip() else prompt
    story = generate_story(final_prompt)
    return story

iface = gr.Interface(
    fn=story_interface,
    inputs=[
        gr.Textbox(label="Main Prompt"),
        gr.Textbox(label="Context (optional)")
    ],
    outputs="text",
    title="🐼 AI Story Generator",
    description="Generate short stories based on your input and optional context."
)

iface.launch()



