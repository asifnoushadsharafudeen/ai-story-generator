import gradio as gr
from generator import generate_story

def story_interface(prompt, context):
    return generate_story(prompt, context)

with gr.Blocks() as demo:
    gr.Markdown("## 📝 AI Story Generator")
    gr.Markdown("Enter a prompt and optionally a context to generate a story!")
    
    with gr.Row():
        prompt_input = gr.Textbox(label="Prompt", placeholder="Enter your story prompt...", lines=2)
        context_input = gr.Textbox(label="Context (optional)", placeholder="Optional background or setting...", lines=2)
    
    output = gr.Textbox(label="Generated Story", lines=10)
    
    submit_btn = gr.Button("Generate")
    clear_btn = gr.Button("Clear")

    submit_btn.click(story_interface, inputs=[prompt_input, context_input], outputs=output)
    clear_btn.click(lambda: ("", "", ""), outputs=[prompt_input, context_input, output])

demo.launch()
