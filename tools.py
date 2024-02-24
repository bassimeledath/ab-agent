from scipy.stats import norm

def sample_size_calculator(confidence=0.95, MDE=0.05, power=0.8, one_sided=True):
    # Convert confidence and power to alpha and beta
    alpha = 1 - confidence
    beta = 1 - power
    
    # Get the Z-scores for the alpha and beta levels
    # For a two-tailed test, we use alpha / 2
    if one_sided:
        Z_alpha = norm.ppf(1 - alpha)
    else:
        Z_alpha = norm.ppf(1 - alpha / 2)
    Z_beta = norm.ppf(1 - beta)
    
    # Standard deviation for a binary outcome under null hypothesis is 0.5 (max variance)
    # This can be adjusted for other distributions or if prior information is available
    std_dev = 0.5
    
    # Calculate sample size using the formula for difference in proportions
    sample_size = ((Z_alpha + Z_beta) ** 2 * (2 * (std_dev ** 2))) / (MDE ** 2)
    
    return round(sample_size)