from transformers import pipeline

# Load GPT-2 model
generator = pipeline("text-generation", model='gpt2')

# ===================== PHASE 2: FastAPI Version (Commented Out) =====================
# def generate_story(prompt: str) -> str:
#     input_text = f"Once upon a time, {prompt}"
#     inputs = tokenizer.encode(input_text, return_tensors="pt")
#     outputs = model.generate(
#         inputs,
#         max_length=150,
#         do_sample=True,
#         temperature=0.9,
#         top_p=0.95,
#         repetition_penalty=1.2
#     )
#     story = tokenizer.decode(outputs[0], skip_special_tokens=True)
#     return story

# ===================== PHASE 3: Gradio Version with Context =========================
def generate_story(prompt, context=None):
    if context and context.strip():
        final_prompt = f"{context.strip()} {prompt.strip()}"
    else:
        final_prompt = prompt.strip()
    
    # Generate story using GPT-2
    result = generator(
        final_prompt,
        max_length=150,
        do_sample=True,
        temperature=0.9,
        top_p=0.95,
        repetition_penalty=1.2
    )
    
    return result[0]["generated_text"]

# ===================== OPTIONAL: CLI Testing Mode (Comment out in Gradio app) =======
# if __name__ == "__main__":
#     print("Welcome to AI Story Generator!\n")
#     user_prompt = input("Enter a story beginning: ")
#     context_input = input("Optional context (press enter to skip): ")
#     if not user_prompt.strip():
#         print("Story cannot be empty. Please try again.")
#     else:
#         story = generate_story(user_prompt, context_input)
#         print("\nGenerated Story:\n")
#         print(story)
