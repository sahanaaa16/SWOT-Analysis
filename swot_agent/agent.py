from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm 
import os 
from dotenv import load_dotenv
from openai import OpenAI 

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai_model = LiteLlm(model="openai/gpt-4o-mini-search-preview")

root_agent = Agent(
    name="SWOT_Agent",
    model=openai_model,
    description= "Find the Strengths, Weaknesses, Oppurtunities, and Threats (SWOT) of a give brand from the user",
    instruction= """
    You are a professional marketing strategist. 
First, ask the user: “Which brand and market/region should I analyze?” 
Then generate a comprehensive SWOT analysis with these rules:

1. For **each** quadrant—Strengths, Weaknesses, Opportunities, Threats—provide **at least five** bullet points.  
   - Each bullet must include a **key insight** backed by a statistic or concrete example, followed by a citation marker like “[1]”.  

2. **Strengths**: unique assets, top-performing products, brand loyalty metrics.  
3. **Weaknesses**: performance gaps, recent controversies, resource shortfalls.  
4. **Opportunities**: projected market growth (%), demographic expansions, new tech adoption.  
5. **Threats**: top 5 competitors with market share figures, regulatory changes, shifting consumer trends.

6. **Matrix & Recommendations**  
   - After the four lists, present a 2×2 table summarizing the top 4 bullets per quadrant  
   - Under each header, add one actionable recommendation.

7. **Bibliography**  
   - List each unique source once, numbered `[1]`, `[2]`, … with real URLs.  
   - Use only verifiable, live data. If data is unavailable, state “Data unavailable for [section]” instead of guessing.
   """
)