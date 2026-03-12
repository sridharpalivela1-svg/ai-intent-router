import json
import os
from openai import OpenAI
from dotenv import load_dotenv
from prompts import PROMPTS

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

LOG_FILE = "logs/route_log.jsonl"


def log_route(intent, confidence, user_message, final_response):

    log_entry = {
        "intent": intent,
        "confidence": confidence,
        "user_message": user_message,
        "final_response": final_response
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")


def route_and_respond(message: str, intent_data: dict):

    intent = intent_data.get("intent")
    confidence = intent_data.get("confidence")

    # Handle unclear intent
    if intent == "unclear":

        response = (
            "I'm not sure what you're asking. "
            "Are you looking for help with coding, data analysis, writing, or career advice?"
        )

        log_route(intent, confidence, message, response)

        return response

    # Select expert prompt
    system_prompt = PROMPTS.get(intent)

    if not system_prompt:
        response = "Sorry, I couldn't determine the correct expert to help you."

        log_route(intent, confidence, message, response)

        return response

    # Call LLM for final response
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ]
    )

    final_response = completion.choices[0].message.content

    # Log routing decision
    log_route(intent, confidence, message, final_response)

    return final_response
