# Automated Python Code Reviewer

This project is an **Automated Python Code Reviewer** that analyzes Python code and provides detailed feedback, including syntax errors, logical issues, and improvement suggestions. The system is built using **Hugging Face Transformers** and **Gradio** for a simple and interactive UI.

## Features

- **Automated Code Review:** Detects syntax and logical errors.
- **AI-Powered Feedback:** Uses a deep learning model to generate insights.
- **User-Friendly Interface:** Built with Gradio for easy interaction.
- **Scalability:** Can be optimized for handling real-world data.

## Technologies Used

- Python
- Transformers (Hugging Face)
- Gradio
- Pretrained Code Generation Model: `Salesforce/codegen-350M-mono`

## Installation

### Prerequisites

Ensure you have Python installed (Python 3.8+ recommended). Install the required dependencies:

```bash
pip install transformers gradio torch
