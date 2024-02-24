
def get_sample_size_prompt(user_query):
    example_prompt = '''
    # Given the user query, provide the design parameters for an A/B test including Confidence Level, Minimum Detectable Effect (MDE), Statistical Power, and Test Type. Below is an example to illustrate how to format your response.

    ## Example
    ### User Query
    Design an A/B test to test a UI change where the metric to increase is browsing time. We want the minimum effect to be 10% and we want to be 95% confident in the results.

    ### Expected Output
    Task: Sample Size Calculation
    Confidence Level: 0.95
    Minimum Detectable Effect (MDE): 0.10
    Statistical Power: 0.8
    Test Type: Two-sided

    ## Example
    ### User Query
    Design an A/B test to test a UI change where the metric to increase is browsing time. We want the minimum effect to be 10% and we want to be 95% confident in the results.

    ### Expected Output
    Task: Sample Size Calculation
    Confidence Level: 0.95
    Minimum Detectable Effect (MDE): 0.10
    Statistical Power: 0.8
    Test Type: Two-sided

    ## User Query
    '''
    # Append the user query and the instruction for expected output
    complete_prompt = example_prompt + user_query + '''
    
    ### Expected Output
    '''
    return complete_prompt

