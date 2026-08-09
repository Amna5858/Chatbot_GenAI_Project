# 🤖 Python CLI Chatbot with Google GenAI

An interactive command-line interface chatbot powered by the **Google GenAI SDK** and the **Gemini 2.5 Flash** model. This project demonstrates clean session-based chat management, exception handling, and environment configuration in Python.

---

## 🚀 Features

* **Interactive CLI Loop:** Seamlessly chat with Gemini directly from your terminal with a continuous conversation flow.
* **Powered by Gemini 2.5 Flash:** Fast, lightweight, and versatile intelligence for natural multi-turn conversations.
* **Built-in Session Memory:** Automatically maintains context throughout your active terminal session.
* **Robust Error Handling:** Gracefully manages keyboard interrupts (`Ctrl+C`), API exceptions, and empty user inputs.
* **Environment Variable Support:** Secures API credentials using `python-dotenv`.

---

## 🛠️ Tech Stack

* **Python 3.13+**
* **Google GenAI SDK** (`google-genai`)
* **Python Dotenv** (`python-dotenv`)

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install Dependencies

Make sure you have Python installed, then install the required packages:

```bash
pip install google-genai python-dotenv
```

### 3. Configure Your API Key

Create a `.env` file in the root directory of your project and add your Google Gemini API key:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

### 4. Run the Chatbot

Navigate to the directory and run the script:

```bash
python chatbot.py
```

---

## 💬 Usage

Once you launch the application, you can start typing your prompts right away.

* To exit the chat at any time, simply type `exit`, `quit`, or `q`.

### Example Session

```text
==================================================
✨ AI-Chatbot initialized using [model_id: gemini-2.5-flash] ....
Type "exit", "quit", "q" to end the conversation.
==================================================
User: Hello!
AI: Hello! How can I help you today?
User: What's the weather like?
AI: I don't have access to real-time weather data, but I can help you understand weather patterns...
User: quit
Exiting the chatbot. Goodbye!
```

---

## 📁 Project Structure

```
your-repo-name/
├── chatbot.py           # Main chatbot script
├── .env                 # Environment variables (create this)
├── .env.example         # Example environment file
├── .gitignore           # Git ignore file
├── requirements.txt     # Python dependencies
├── LICENSE              # MIT License
└── README.md            # This file
```

---

## 🔧 Configuration

### Environment Variables

The `.env` file should contain:

```env
GEMINI_API_KEY=your_google_gemini_api_key
```

**Note:** Never commit your `.env` file to version control. Use `.env.example` as a template for others.

---

## 🚨 Error Handling

The chatbot gracefully handles:

* **Keyboard Interrupts:** Press `Ctrl+C` to exit safely
* **API Errors:** Displays meaningful error messages if the API is unavailable
* **Empty Input:** Skips empty prompts and continues the conversation
* **Connection Issues:** Retries or notifies users of network problems

---

## 📚 How It Works

1. **Initialization:** Loads the Google GenAI client with your API key
2. **Session Loop:** Continuously accepts user input
3. **Message Processing:** Sends messages to Gemini 2.5 Flash model
4. **Response Display:** Streams and displays AI responses in real-time
5. **Context Preservation:** Maintains conversation history within the session
6. **Exit Handling:** Cleanly closes the connection on user request

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 🙋 Support

If you encounter any issues:

1. Check that your API key is valid
2. Ensure Python 3.13+ is installed
3. Verify all dependencies are installed: `pip install -r requirements.txt`
4. Check your internet connection
5. Review the error message in the console

For more help, open an issue on GitHub.

---

## 🎯 Future Enhancements

* [ ] Save conversation history to file
* [ ] Command-line arguments for custom models
* [ ] Multi-session support
* [ ] Custom prompt templates
* [ ] Conversation logging and analytics
* [ ] Docker containerization

---

## 📝 Notes

* This chatbot uses the **Gemini 2.5 Flash** model for fast, efficient responses
* Conversations are stored in memory only (not persisted between sessions)
* API usage is subject to Google's rate limits and pricing

---

**Happy chatting! 🎉**
