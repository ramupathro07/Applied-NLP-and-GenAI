from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_llm_response(prompt, model="openai/gpt-oss-20b"):
    """
    This function sends prompt to Groq LLM and returns the response.
    """
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
    "role": "system",
    "content": "You are a helpful assistant that only outputs valid JSON. Never add any text outside the JSON object."
},
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model=model,
            temperature=0.1,
            response_format={"type": "json_object"}
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return json.dumps({"error": str(e)})