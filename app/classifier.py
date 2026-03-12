import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


CLASSIFIER_PROMPT = """
Your task is to classify the user's intent.

Choose one of the following labels:
code
data
writing
career
unclear

Respond ONLY with a JSON object with this format:

{
 "intent": "label",
 "confidence": 0.0
}

Confidence must be between 0.0 and 1.0.

Do not include any text outside the JSON.
"""


def classify_intent(message: str):

    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": CLASSIFIER_PROMPT},
                {"role": "user", "content": message}
            ]
        )

        result = response.choices[0].message.content

        parsed = json.loads(result)

        return {
            "intent": parsed.get("intent", "unclear"),
            "confidence": float(parsed.get("confidence", 0.0))
        }

    except Exception:

        return {
            "intent": "unclear",
            "confidence": 0.0
        }
