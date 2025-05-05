# 🌟 Browser Use Controller with LangChain + Gemini

Welcome to the **Browser Use Controller** project! This powerful tool uses **LangChain**, **Gemini**, and **asyncio** to automate tasks within your browser. It simulates human-like actions, such as searching YouTube, playing videos, and gathering information—all powered by Google's **Gemini API**.

![Browser Use Controller](https://img.shields.io/badge/Project-Browser%20Use%20Controller-brightgreen)  
![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)  
![License](https://img.shields.io/badge/License-MIT-blue)  

---

## 📽️ Demo Videos

### 🎥 **Setup Environment**  
[![Watch on YouTube](https://img.youtube.com/vi/P08Ho_osy8g/0.jpg)](https://youtu.be/P08Ho_osy8g)

### 🎥 **Running the Agent & Performance**  
[![Watch on YouTube](https://img.youtube.com/vi/N78LQqna5ZE/0.jpg)](https://youtu.be/N78LQqna5ZE)

---

## 🚀 Features

- **Powerful integration** with **LangChain** and **Google Gemini Flash Model**.
- Automates browser tasks with a custom-built **Agent** class.
- Fully asynchronous with **asyncio** for enhanced performance.
- Easy to customize for your own tasks and needs.

---

## 📦 Installation & Setup

### ✅ **Prerequisites**

- Python **3.8+**
- Git
- **Google Gemini API Key** (store it in a `.env` file as `GEMINI_API_KEY`)

### 🔧 **Environment Setup**

1. Clone the repository:
    ```bash
    git clone https://github.com/SARAMALI15792/browser_use_controller.git
    cd browser_use_controller
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv browser-agent
    browser-agent\Scripts\activate         # On Windows
    # or
    source browser-agent/bin/activate     # On Mac/Linux
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the API Key:**

    Create a `.env` file in the root directory with the following content:

    ```env
    GEMINI_API_KEY=your_gemini_api_key_here
    ```

---

## 🧠 **How It Works**

1. **Load the API Key**: Loads the **Gemini API** key from the environment variable.
2. **Initialize the Model**: Sets up the **ChatGoogleGenerativeAI** model using the `gemini-2.0-flash` model.
3. **Agent Execution**: Creates a browser **Agent** that performs specific tasks (e.g., searching YouTube and playing videos).
4. **Async Operation**: Runs asynchronously using **asyncio** to maximize performance.

---

## 🏃‍♂️ **Usage**

After setting up, run the following command to start the agent:

```bash
uv run main.py
```

The agent will:
- Open a browser window
- Search YouTube for *CampusX*
- Play the LangChain video
- Return details about the channel and person

---

## 🔧 **Customize Task**

To modify the task the agent performs, edit the `task` argument in `main.py`:

```python
task="your new task here"
```

For example:
```python
task="go to Google and find the latest news about AI"
```

---

## 📄 **License**

This project is licensed under the **MIT License**. You are free to use, modify, and distribute it.

---

## ✨ **Author**

**Saram Ali**  
[LinkedIn]([https://www.linkedin.com/in/saram-ali](https://www.linkedin.com/in/saram-ali-099b9b2a4/)) | [GitHub](https://github.com/SARAMALI15792)

---

### 📚 Additional Resources

- [LangChain Documentation](https://langchain.com/docs)
- [Gemini API Documentation](https://developers.google.com/ai/gemini)

---
