from models import *

def get_backend_response(user_query, csv=False):

    if not csv:
        updated_prompt = mistral_text_complete(user_query, sample_size=True)
    else:
        updated_prompt = mistral_text_complete(user_query, sample_size=False)

    return function_call_agent(updated_prompt)