Here is the content for your GitHub repository (**description** and **README.md** file) tailored for your CLI chatbot project:

---

### **Repository Description**

> A command-line interface (CLI) chatbot built in Python using the Google GenAI SDK (`gemini-2.5-flash`), featuring interactive conversation loops, session history, and robust error handling.

---

### **README.md**

```markdown
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
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
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

```text
==================================================
✨ AI-Chatbot initialized using [model_id: gemini-2.5-flash] ....
Type "exit", "quit", "q" to end the conversation. \n
==================================================

User: Hello!
AI: Hello! How can I help you today?
User: quit
Exiting the chatbot. Goodbye!

```

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

```

```
