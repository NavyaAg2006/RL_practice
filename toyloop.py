# guess number

import os
import json
import random
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "openai/gpt-oss-120b"

GUESS_TOOL = {"name": "guess", "description": "Guess the secret number",
"parameters": {"type": "object",
"properties": {"n": {"type": "integer"}},
"required": ["n"]}}

class GuessEnv:
    def reset(self,seed=None):
        self.secret = random.Random(seed).randint(1,100)
        self.steps,self.solved=0,False
        return "Find a number from 1 to 100 using Guess tool"

    def step(self,n):
        self.steps+=1
        if self.secret == n:
            self.solved=True
            return "Correct!",True
        hint = "higher" if self.secret > n else "lower"
        return f"try {hint}",self.steps>=10

    def verify(self):
        return 1.0 - 0.05 * self.steps if self.solved else 0.0

def run_game(seed=None):
    env = GuessEnv()
    task = env.reset(seed)

    messages = [{"role": "user", "content": task}]

    tools = [{
        "type": "function",
        "function": GUESS_TOOL
    }]

    done = False

    while not done:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=tools,
            tool_choice="required"
        )

        msg = response.choices[0].message
        messages.append(msg)

        for call in msg.tool_calls or []:
            args = json.loads(call.function.arguments)
            n = args["n"]

            result, done = env.step(n)
            print(f"Guess {env.steps}: {n} -> {result}")

            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": result
            })

            if done:
                break

    score = env.verify()
    print(f"Solved: {env.solved}")
    print(f"Secret: {env.secret}")
    print(f"Score: {score:.2f}")

    return score


if __name__ == "__main__":
    run_game(seed=42)
