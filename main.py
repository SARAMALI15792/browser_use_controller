from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from dotenv import load_dotenv
import os
import asyncio
# Read GEMINI_API_KEY into env
load_dotenv()
key = os.getenv("GEMINI_API_KEY")
# Initialize the model
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash',
                            temperature=1,
                            timeout=100,
                            api_key=key,
)

async def main():
    # Create agent with the model
    agent = Agent(
        task="""
        
        Task Overview
Please execute the following steps in order:

Create Google Account:

Navigate to Google Account creation.

Register a new personal Google account with the following details:

First Name: Sahil

Last Name: Kumar

Email: sahilkumar15792@gmail.com

Password: sahil123

Send Email Notification:

After account creation, log into the newly created Gmail account.

Compose and send an email to: saramali15792@gmail.com

Subject: Account Created

Body: Write something about browser-use agent.

ChatGPT Signup and Interaction:

Go to ChatGPT and sign up using the created Gmail account.

After successful signup and login, ask a Python-related question in ChatGPT
             
             
              """,      
         
         llm=llm
    )
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())