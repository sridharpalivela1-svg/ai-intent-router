# AI Intent Router

## Overview

This project implements an **intent-based AI prompt router** that intelligently directs user requests to specialized AI personas. Instead of using one large generic prompt, the system first classifies the user’s intent and then routes the request to an expert prompt designed for that task.

The application demonstrates a common architecture used in modern AI systems: **Classify → Route → Generate**.

---

## Features

* Intent classification using an LLM
* Routing requests to specialized expert prompts
* Four expert personas:

  * Code Expert
  * Data Analyst
  * Writing Coach
  * Career Advisor
* Handles unclear user intent with clarification questions
* Logs every routing decision and response
* Docker containerization for easy deployment

---

## System Architecture

The system works in two stages:

1. **Intent Classification**

   * The user message is sent to a lightweight LLM prompt.
   * The model returns a JSON object containing:

   ```
   {
     "intent": "code",
     "confidence": 0.92
   }
   ```

2. **Prompt Routing**

   * The system selects the correct expert prompt based on the detected intent.
   * The message is sent again to the LLM using the specialized prompt.
   * The final response is returned to the user.

---

## Supported Intents

| Intent  | Persona                     |
| ------- | --------------------------- |
| code    | Software engineering expert |
| data    | Data analysis specialist    |
| writing | Writing improvement coach   |
| career  | Career advisor              |
| unclear | Ask clarification           |

---

## Project Structure

```
ai-intent-router
│
├── app
│   ├── main.py
│   ├── classifier.py
│   ├── router.py
│   └── prompts.py
│
├── logs
│   └── route_log.jsonl
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .env.example
```

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/ai-intent-router.git
cd ai-intent-router
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Create environment file

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

### 4. Run the application

```
python app/main.py
```

---

## Running with Docker

Build and run the application using Docker:

```
docker compose up --build
```

---

## Logging

Every request is logged to:

```
logs/route_log.jsonl
```

Each log entry contains:

```
{
 "intent": "code",
 "confidence": 0.91,
 "user_message": "...",
 "final_response": "..."
}
```

---

## Example Test Inputs

Some example messages used to test the system:

* how do i sort a list of objects in python?
* explain this sql query for me
* This paragraph sounds awkward, can you help me fix it?
* I'm preparing for a job interview, any tips?
* what's the average of these numbers: 12, 45, 23, 67, 34
* Help me make this better.
* I need to write a function that takes a user id and returns their profile.
* hey
* Can you write me a poem about clouds?
* Rewrite this sentence to be more professional.
* I'm not sure what to do with my career.
* what is a pivot table
* fxi thsi bug pls: for i in range(10) print(i)
* How do I structure a cover letter?
* My boss says my writing is too verbose.

---

## Design Decisions

* Separate classifier and generator prompts for better performance.
* JSON-based classifier output for reliable routing.
* Logging system for observability and debugging.
* Docker containerization for reproducible environments.

---

## Environment Variables

Example `.env.example`:

```
OPENAI_API_KEY=your_api_key_here
```

---

## Future Improvements

* Confidence threshold for intent classification
* Manual override using prefixes like `@code`
* Web interface using Flask or FastAPI
* Additional expert personas
