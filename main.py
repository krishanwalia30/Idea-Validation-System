import os
import dspy
from modules import *
import time
from dotenv import load_dotenv
import google.generativeai as genai
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# Load environment variables from the .env file
load_dotenv()
from utils import search_market

# Initialize FastAPI app
app = FastAPI()

# Initialize models and configurations
# gemini = dspy.Google(model='gemini-flash-latest', api_key=os.environ["GOOGLE_API_KEY"], temperature=0.3)
gemini = dspy.Google(model='gemini-2.5-flash-lite', api_key=os.environ["GOOGLE_API_KEY"], temperature=0.3)
dspy.settings.configure(lm=gemini)

chatbot = CoT()
keyword = KeywordGenerator()
fab = FinalAnswerBot()

# Define request model
class MarketResearchRequest(BaseModel):
    topic: str
    description: str

@app.post("/market-research")
async def get_market_research(request: MarketResearchRequest):
    try:
        # Generate keywords
        generated_keywords = keyword(topic=request.topic, description=request.description)
        list_of_keywords = generated_keywords.keywords.split(",")
        list_of_keywords.append(request.topic)

        # Generate market research for each keyword
        all_generated_response = []
        for key in list_of_keywords:
            # Search market discussions
            market_discussion = search_market(key)
            
            # Generate summary
            response = chatbot(topic=key, description=request.description, discussion=market_discussion)
            all_generated_response.append(response.answer)
            
            # Add delay to prevent rate limiting
            time.sleep(5)

        # Generate final summary
        final_summary = fab(
            topic=request.topic, 
            description=request.description,
            keywords=str(list_of_keywords),
            summaries=str(all_generated_response)
        )

        return {
            "status": "success",
            "market_research": final_summary.answer,
            "keywords": list_of_keywords
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)