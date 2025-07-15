import os
from dotenv import load_dotenv
from google import genai
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

arguments = sys.argv[1:]
if not arguments:
    print("No argument!")
    sys.exit(1)

verbose = False
if "--verbose" in arguments:
    verbose = True
    arguments.remove("--verbose")

prompt = " ".join(arguments)
response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=prompt
)

if verbose:
    print("User prompt:", prompt)
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)
