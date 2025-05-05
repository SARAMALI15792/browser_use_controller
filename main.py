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
        task="go on youtube and search for campusx and play the lanchain video and give me the view about the channel and person name also !!",
        llm=llm
    )
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())