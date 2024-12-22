import gradio as gr
from transformers import pipeline
import random

# Load preset prompts
file_name = "philosophical_questions.txt"
with open(file_name, "r") as file:
    philosophical_questions = [line.strip() for line in file]

# Function to load the appropriate text generation pipeline
def get_generator(model_name: str):
    return pipeline("text-generation", model=model_name)

def generate_text(model_name: str, prompt: str, style: str, temperature: float, max_length: int, top_p: float, top_k: int) -> str:
    generator = get_generator(model_name)
    do_sample = temperature != 0
    prompt = prompt + "Answer in a " + style + "way."
    response = generator(prompt, max_new_tokens=max_length, temperature=temperature, top_p=top_p, do_sample=do_sample,
                         top_k=top_k)
    response = response[0]['generated_text'].replace(prompt, "", 1).strip()
    return response

def random_prompt():
    return random.choice(philosophical_questions)


with gr.Blocks(title="PhiloGPT") as demo:
    gr.Markdown("# PhiloGPT - Philosophical GPT to explore GenAI in an interesting way")
    gr.Markdown(
        "Generate text using GPT models with customizable parameters. Use the random prompt generator to explore ideas!")

    with gr.Row():
        prompt = gr.Textbox(label="Prompt", lines=5, placeholder="Enter a philosophical question to generate text about...")
        random_button = gr.Button("Random Philosophical Question")

    model = gr.Radio(choices=["gpt2", "distilgpt2"], label="Select Model", value="gpt2")

    style = gr.Dropdown(choices=["funny", "optimistic", "stoic", "sarcastic"], label="Select Style",
                        value="funny")

    temperature = gr.Slider(value=1, minimum=0, maximum=2, step=0.1, label="Temperature",
                            info="Adjusts randomness: higher for creativity, lower for predictability.")
    max_length = gr.Slider(value=150, minimum=1, maximum=256, step=1, label="Max. length",
                           info="Sets the maximum number of words for the generated text.")
    top_p = gr.Slider(value=1, minimum=0, maximum=1, step=0.1, label="Top p",
                      info="Narrows or broadens the choice of next words based on their likelihood.")
    top_k = gr.Slider(value=50, minimum=1, maximum=100, step=1, label="Top k",
                      info="Number of highest probability vocabulary tokens to keep for top-k filtering.")

    generate_button = gr.Button("Generate Text")
    output = gr.Textbox(label="Generated text")

    # Define interactions
    random_button.click(fn=random_prompt, inputs=[], outputs=prompt)
    generate_button.click(fn=generate_text, inputs=[model, prompt, style, temperature, max_length, top_p, top_k], outputs=output)

demo.launch()

