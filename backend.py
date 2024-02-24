from models import *

def get_backend_response(user_query, csv=False):
    if not csv:
        updated_prompt = mistral_text_complete(user_query, sample_size=True)
        sample_size_result = function_call_agent(updated_prompt)
        lines = updated_prompt.split('\n')  # Splitting the printed text into lines
        results_dict = {}
        for line in lines[1:]:
            if line:  # Check if the line is not empty
                key, value = line.split(': ')
                results_dict[key.strip()] = float(value) if key != "Test Type" else value
        
        # Adding the sample size to the dictionary
        results_dict["Sample Size"] = sample_size_result
        
        return results_dict

    else:
        updated_prompt = calculate_significance_and_save("simulated_data.csv", "variation", "browse_time")
        print(updated_prompt)
        # function_call_agent("interpret the results:" + updated_prompt))
        return ["output_data.csv", "Decision: Go with feature B as is statistically significanlty better than feature A"]
    