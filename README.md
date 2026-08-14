# Terminal AI Chatbot

A terminal-based AI chatbot built with Python that integrates the **Groq API** to process user input and generate AI-powered responses.

## Features

* 💬 Interactive terminal-based chat
* 🤖 AI-powered responses using the Groq API
* 🔐 API key stored securely using environment variables
* ⚡ Fast response generation through Groq
* 🐍 Built with Python
* 🛑 Simple command to exit the chatbot

## Technologies Used

* **Python**
* **Groq API**
* **python-dotenv**

## Project Structure

```text
terminal-ai-chatbot/
│
├── main.py
├── .env
├── .gitignore
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd terminal-ai-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file in the project directory:

```env
GROQ_API_KEY=your_api_key_here
```

Make sure `.env` is included in `.gitignore` so your API key is not uploaded to GitHub.

### 5. Run the chatbot

```bash
python main.py
```

## Example

```text
You: What is Python?

AI: Python is a high-level, general-purpose programming language...
```

## How It Works

1. The user enters a message in the terminal.
2. Python receives the user's input.
3. The input is sent to the Groq API.
4. The AI processes the request.
5. The generated response is displayed in the terminal.

## Future Improvements

* Add conversation history
* Add streaming responses
* Add different AI model options
* Add a graphical user interface
* Add voice input and output
* Improve error handling
* Add chat history storage

## License

This project is for learning and educational purposes.
