import os
from dotenv import load_dotenv
load_dotenv()



from langchain.chat_models import init_chat_model

#GEMINI
gemini = init_chat_model(
    model="gemini-3.1-flash-lite",
    model_provider="google_genai",
    # api_key = os.environ.get('GOOGLE_API_KEY')
)
