# 🔍 Browser Use Controller with LangChain + Gemini

This project is a browser automation agent using `LangChain`, `Gemini`, and `asyncio`. It simulates human-like behavior to complete tasks on the browser, such as searching YouTube and retrieving information — all powered by Google's Gemini API.

---

## 📽️ Demo Videos

### 📌 Video 1: Setup Environment and Code  
[![Watch on YouTube](https://img.youtube.com/vi/P08Ho_osy8g/0.jpg)](https://youtu.be/P08Ho_osy8g?si=zuKSfvW8jnxWXeM1)

### 📌 Video 2: Running the Agent & Performance  
[![Watch on YouTube](https://img.youtube.com/vi/N78LQqna5ZE/0.jpg)](https://youtu.be/N78LQqna5ZE)

---

## 🚀 Features

- Uses **LangChain** with **Google Gemini Flash Model**
- Automates browser actions using the custom `Agent` class
- Async-powered execution for efficient task handling

---

## 📦 Installation & Setup

### ✅ Prerequisites

- Python 3.8+
- Git
- Google Gemini API Key (store it in a `.env` file as `GEMINI_API_KEY`)

### 🔧 Environment Setup

```bash
git clone https://github.com/SARAMALI15792/browser_use_controller.git
cd browser_use_controller
python -m venv browser-agent
browser-agent\Scripts\activate         # On Windows
# or
source browser-agent/bin/activate     # On Mac/Linux
pip install -r requirements.txt
```

Create a `.env` file in the root folder and add:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## 🧠 How It Works

1. Loads the Gemini API key from environment variables.
2. Initializes a `ChatGoogleGenerativeAI` model.
3. Creates a browser `Agent` that performs a task (e.g., YouTube search).
4. Runs asynchronously to avoid blocking operations.

---

## 🏃‍♂️ Usage

After setup, just run:

```bash
uv run main.py
```

The agent will:
- Open a browser
- Search YouTube for *CampusX*
- Play the LangChain video
- Return insights about the channel and person

---

## 🛠️ Customize Task

To change the task the agent performs, edit this line in `main.py`:

```python
task="your new task here"
```

Example:
```python
task="go to Google and find the latest news about AI"
```

---

## 📄 License

This project is for educational and experimental purposes.

---

## ✨ Author

**Saram Ali**
