# improved_automated_code_reviewer.py

import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Define the model name (using Salesforce CodeGen for Python)
MODEL_NAME = "Salesforce/codegen-350M-mono"

# Load the tokenizer and model from Hugging Face Hub
print("Loading model and tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

# Create a text-generation pipeline using the loaded model and tokenizer
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def review_code(input_code: str) -> str:
    """
    Takes Python code as input and returns a detailed review of the code.
    The review includes identification of any syntax or logical errors, an explanation of the issues,
    and suggestions for improvements.
    """
    # Updated prompt with explicit instructions
    prompt = (
        "You are an expert Python code reviewer. Please analyze the following Python code and provide a detailed review that includes:\n"
        "1. Identification of any syntax errors, logical errors, or potential runtime issues.\n"
        "2. A clear explanation of each issue, including why it is problematic.\n"
        "3. Specific suggestions for improvements or corrections.\n\n"
        "Python Code:\n"
        f"{input_code}\n\n"
        "Review:"
    )
    
    # Generate the review using the Hugging Face text generation pipeline.
    output = generator(prompt, max_length=500, num_return_sequences=1)
    
    # Extract and clean the generated text by removing the prompt portion
    generated_text = output[0]["generated_text"]
    review = generated_text[len(prompt):].strip()
    return review

# Set up the Gradio interface
iface = gr.Interface(
    fn=review_code,
    inputs=gr.Textbox(lines=20, label="Enter Python Code"),
    outputs=gr.Textbox(label="Code Review"),
    title="Automated Python Code Reviewer",
    description=(
        "Paste your Python code below to receive a detailed review. The review will identify syntax and logical errors "
        "and provide suggestions for improvements."
    )
)

if __name__ == "__main__":
    # Launch the Gradio app on a local server.
    iface.launch()
