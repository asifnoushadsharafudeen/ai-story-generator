# 🤖 AI Story Generator using GPT-2

This project is part of my Generative AI Engineering Portfolio. It uses OpenAI’s **GPT-2** model via Hugging Face Transformers to generate short creative stories based on user-provided prompts. The project is structured in two phases:

---

## ✅ Phase 1 – Auto Story Generator (Python Script)

A basic script that generates a story given a prompt using GPT-2.

### Features
- Automatically generates a story from a custom prompt.
- Uses GPT-2 via Hugging Face Transformers.
- Tuned for creativity and coherence (`temperature`, `top_p`, `repetition_penalty`).

### File
- `generator.py` – contains the `generate_story()` function.

---

## 🚀 Phase 2 – FastAPI Integration (API Serving)

A FastAPI app that exposes a `/generate` POST endpoint. You send a prompt via JSON, and it returns a generated story.

### Features
- Backend API using FastAPI.
- Accepts JSON input (`prompt`) and returns story as JSON.
- Swagger UI supported for easy testing.

### File
- `main.py` – FastAPI application with POST endpoint.

---

## 🧠 Tech Stack

| Tool / Library          | Purpose                                |
|-------------------------|----------------------------------------|
| Python                  | Programming language                   |
| Hugging Face Transformers | GPT-2 text generation                |
| FastAPI                 | Backend API server                     |
| Uvicorn                 | ASGI server for running FastAPI apps   |
| Pydantic                | Input data validation                  |

---