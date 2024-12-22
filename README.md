# PhiloGPT

PhiloGPT is a Gradio-based application designed to explore generative AI in an interesting way. 
Users can input their own philosophical prompts or use a built-in random question generator that selects a random question of a predefined list, customize the style of the AI's response, and select from various GPT models for text generation.

## Features

- **Model Selection**: Choose between models like `gpt2`, or `distilgpt2`, for generating text.
- **Style Customization**: Modify the tone of the response with options such as `funny`, `optimistic`, `stoic`, or `sarcastic`.
- **Random Prompts**: Generate philosophical questions randomly from a predefined list.
- **Customizable Parameters**: Adjust text generation parameters like temperature, max length, top-p, and top-k to influence creativity and predictability.

## Getting Started

### Prerequisites

- Python 3.8 or later
- Required Python packages:
  - `gradio`
  - `transformers`
  - `torch`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/philoGPT.git
   ```

2. Navigate to the project directory:
   ```bash
   cd philoGPT
   ```
   
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure you have a file named `philosophical_questions.txt` in the project directory. This file should contain one question per line.

### Running the App

1. Launch the application:
   ```bash
   python main.py
   ```

2. Open the provided local URL (e.g., `http://127.0.0.1:7860`) in your browser.

3. Interact with the app:
   - Enter your own philosophical question in the prompt box or select a random question.
   - Customize the model and style.
   - Adjust text generation parameters and generate your response.

### Example

1. Input: "What is the meaning of life?"
2. Style: `funny`
3. Model: `gpt2`
4. Parameters: Temperature = 1.2, Max Length = 50
5. Output: "Life is just one long comedy show with a twist: you're the main character, and you don't have the script."

## Screenshots
Here are two screenshots that showcase the functionality of PhiloGPT:
![Screenshot1.png](screenshots%2FScreenshot1.png)
![Screenshot2.png](screenshots%2FScreenshot2.png)
Additional screenshots are available in the `screenshots` folder.

## Motivation
Understanding the fundamental mechanisms of generative AI is crucial in demystifying its capabilities. It is not magic, nor is it a replacement for human creativity. Instead, generative AI should be viewed as a powerful tool that complements and enhances human thought, enabling new possibilities and perspectives. However, its use must be approached with caution and responsibility, ensuring it serves as a supporting aid rather than a substitute for critical thinking and originality.


## Acknowledgments
- [Hugging Face Transformers](https://huggingface.co/transformers/) for the text generation models.
- [Gradio](https://gradio.app/) for the user-friendly interface.

