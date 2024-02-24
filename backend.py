from models import *

def get_backend_response(user_query, csv=False):
    if not csv:
        updated_prompt = mistral_text_complete(user_query, sample_size=True)
        sample_size_result = function_call_agent(updated_prompt)
        lines = updated_prompt.split('\n')  # Splitting the printed text into lines
        results_dict = {}
        for line in lines:
            if line:  # Check if the line is not empty
                key, value = line.split(': ')
                results_dict[key.strip()] = float(value) if key != "Test Type" else value
        
        # Adding the sample size to the dictionary
        results_dict["Sample Size"] = sample_size_result
        
        return results_dict

        
    else:
        updated_prompt = mistral_text_complete(user_query, sample_size=False)
        return None

    