import pandas as pd
from llama_index.core.query_engine import PandasQueryEngine
from fireworks.client import Fireworks
import os
import json
from scipy.stats import norm
from dotenv import load_dotenv
from tools import *
from prompts import *
import matplotlib.pyplot as plt
import openai
load_dotenv()

def mistral_text_complete(prompt, sample_size=True):
    if sample_size:
        updated_prompt = get_sample_size_prompt(prompt)
    else:
        updated_prompt = prompt  # Or handle differently if sample_size is False

    # Initialize the Fireworks client with your API key
    client = Fireworks(api_key=os.getenv('FIREWORKS_API_KEY'))
    
    # Make a request to the API with the provided prompt
    response = client.chat.completions.create(
        model="accounts/fireworks/models/mixtral-8x7b-instruct",
        messages=[{
            "role": "user",
            "content": updated_prompt,
        }],
        temperature=0
    )
    
    # Return the content of the first choice in the response
    # Make sure to handle potential errors or check response status as needed
    return response.choices[0].message.content

def pandas_agent_complete(query, df):
    """
    Executes a query on the provided DataFrame using the PandasQueryEngine from the llama_index package.

    Parameters:
    - query: A string representing the query to be executed.
    - df: The pandas DataFrame on which the query will be executed.

    Returns:
    - The response from executing the query on the DataFrame.
    """
    # Initialize the PandasQueryEngine with the provided DataFrame and verbosity enabled
    query_engine = PandasQueryEngine(df=df, verbose=False)
    
    # Execute the query and store the response
    response = query_engine.query(query)
    
    # Return the response obtained from the query
    return response

def hists(df):
        a_df = df[df['variation'] == 'A']['browse_time']
        b_df = df[df['variation'] == 'B']['browse_time']

        plt.figure()
        plt.hist(a_df)
        plt.savefig('a_hist.png')

        plt.figure()
        plt.hist(b_df)
        plt.savefig('b_hist.png')

        return ['a_hist.png', 'b_hist.png']

def function_call_agent(prompt):
    ## tools
    def sample_size_calculator(confidence=0.95, MDE=0.05, power=0.8, one_sided=False):
        alpha = 1 - confidence
        beta = 1 - power
        if one_sided:
            Z_alpha = norm.ppf(1 - alpha)
        else:
            Z_alpha = norm.ppf(1 - alpha / 2)
        Z_beta = norm.ppf(1 - beta)
        std_dev = 0.5
        sample_size = ((Z_alpha + Z_beta) ** 2 * (2 * (std_dev ** 2))) / (MDE ** 2)
        
        return round(sample_size)

    # Load tools configuration from tools.json
    with open('tools.json', 'r') as file:
        tools = json.load(file)
    client = openai.OpenAI(
        base_url="https://api.fireworks.ai/inference/v1",
        api_key=os.getenv("FIREWORKS_API_KEY")
    )
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant with access to functions. Use them if required."},
        {"role": "user", "content": prompt}
    ]
    
    chat_completion = client.chat.completions.create(
        model="accounts/fireworks/models/firefunction-v1",
        messages=messages,
        tools=[tools],
        temperature=0
    )
    
    # Extract the function call and arguments from the response
    function_call = chat_completion.choices[0].message.tool_calls[0].function
    # Execute the corresponding function dynamically
    tool_response = locals()[function_call.name](**json.loads(function_call.arguments))

    return tool_response



