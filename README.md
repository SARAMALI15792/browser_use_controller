# 🌟 Browser Use Controller with LangChain + Gemini

Welcome to the **Browser Use Controller** project! This tool uses **LangChain**, **Gemini**, and **asyncio** to automate browser tasks. It can simulate human-like actions, like searching YouTube and gathering information, all powered by Google's **Gemini API**.

![Project Badge](https://img.shields.io/badge/Project-Browser%20Use%20Controller-brightgreen)  
![Python Badge](https://img.shields.io/badge/Python-3.8%2B-blue)  
![License Badge](https://img.shields.io/badge/License-MIT-blue)  

---

## 📽️ Demo Videos

### 🎥 **Setup Video**  
[![Watch on YouTube](https://img.youtube.com/vi/P08Ho_osy8g/0.jpg)](https://youtu.be/P08Ho_osy8g)

### 🎥 **Running the Agent**  
[![Watch on YouTube](https://img.youtube.com/vi/N78LQqna5ZE/0.jpg)](https://youtu.be/N78LQqna5ZE)

---

## 🚀 Features

- Powered by **LangChain** and **Google Gemini Flash Model**
- Automates tasks in the browser using a custom **Agent**
- Fast and efficient with **asyncio** (asynchronous execution)
- Easy to customize for different tasks

---

## 📦 Installation & Setup

### ✅ Requirements

- Python **3.8+**
- Git
- **Google Gemini API Key** (you’ll need to add it to a `.env` file)

### 🔧 How to Set Up

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

3. Install the necessary libraries:
    ```bash
    pip install -r requirements.txt
    ```

4. **Add your API Key**:

    Create a `.env` file in the main folder and add your Gemini API key like this:

    ```env
    GEMINI_API_KEY=your_gemini_api_key_here
    ```

---

## 🧠 How It Works

1. The **Gemini API Key** is loaded from the environment.
2. A **ChatGoogleGenerativeAI** model is created using **Google's Gemini Flash**.
3. The **Agent** executes tasks based on the prompt you provide. For example, you can tell the agent to search for a specific YouTube channel and gather information about it.
4. It runs asynchronously using **asyncio** for smooth performance.

---

## 🏃‍♂️ How to Run It

Once set up, run the following command:

```bash
uv run main.py
```

The agent will:
- Open a browser window
- Search YouTube for *CampusX* (or any prompt you set)
- Play the LangChain video
- Show insights about the channel and person

---

## 🛠️ Customize the Task

To change what the agent does, edit the `task` in the `main.py` file:

```python
task="your new task here"
```

For example:
```python
task="search for the latest AI news on Google"
```

In your case, you can set the task to search for a specific **YouTube channel**, like this:
```python
task="search for the CampusX YouTube channel, play a video, and return the channel information"
```

---

## 📄 License

This project is licensed under the **MIT License**, which means you can use, modify, and share it freely.

---

## ✨ Author

**Saram Ali**  
[LinkedIn](https://www.linkedin.com/in/saram-ali-099b9b2a4/) | [GitHub](https://github.com/SARAMALI15792)

---

### 📚 Additional Resources

- [LangChain Docs](https://langchain.com/docs)
- [Gemini API Docs](https://developers.google.com/ai/gemini)

---
