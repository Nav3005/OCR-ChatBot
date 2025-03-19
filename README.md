# OCR Chatbot

This project is a **OCR Chatbot** built using **Streamlit** and **Google's Gemini API**. It allows users to interact with the chatbot using both text and images.

## Features

- **Text and Image-Based Queries**: Supports both textual and image-based questions.
- **Google Gemini API Integration**: Uses `gemini-2.0-flash` for generating responses.
- **Streamlit UI**: Provides an interactive web interface.
- **Environment Variables Support**: Loads API keys securely from `.env`.

## Prerequisites

Ensure you have the following installed:

```bash
pip install streamlit google-generativeai python-dotenv pillow
```

Additionally, set up your **Google API Key** in a `.env` file:

```env
Google_API_KEY=your_api_key_here
```

## Usage

Run the chatbot with:

```bash
streamlit run ocr.py
```

## How It Works

1. Loads the **Google API key** from the `.env` file.
2. Initializes **Gemini-2.0-flash** model for text and image processing.
3. Provides a Streamlit UI for user interaction.

## Customization

- Modify the **model selection** (`gemini-2.0-flash`).
- Adjust **UI elements** in `streamlit` for better usability.
- Extend functionality for **image analysis and response generation**.

## License

This project is licensed under the MIT License.

---

### 🚀 Feel free to contribute and enhance the chatbot!
