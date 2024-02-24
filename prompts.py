
def get_sample_size_prompt(user_query):
    example_prompt = '''
    # Given the user query, provide the design parameters for an A/B test including Confidence Level, Minimum Detectable Effect (MDE), Statistical Power, and Test Type. Below is an example to illustrate how to format your response.

    ## Example
    ### User Query
    Design an A/B test to evaluate the impact of a new homepage layout on user engagement, measured by click-through rate (CTR). We aim for a minimum detectable effect (MDE) of 5% increase in CTR with a confidence level of 95%.

    ### Expected Output
    Confidence Level: 0.95
    Minimum Detectable Effect (MDE): 0.05
    Statistical Power: 0.8
    Test Type: Two-sided

    ## User Query
    '''
    # Append the user query and the instruction for expected output
    complete_prompt = example_prompt + user_query + '''
    
    ### Expected Output
    '''
    return complete_prompt