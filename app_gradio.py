import gradio as gr
from generator import generate_story

def generate_with_prompt(prompt):
    return generate_story(prompt)

iface = gr.Interface(
    fn=generate_with_prompt,
    inputs=gr.Textbox(lines=2, placeholder="Enter your story prompt..."),
    outputs="text",
    title="📝 AI Story Generator",
    description="Enter a prompt and let GPT-2 generate a story for you!"
)

if __name__ == "__main__":
    iface.launch()
