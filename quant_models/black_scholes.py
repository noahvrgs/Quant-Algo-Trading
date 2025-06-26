import numpy as np
from scipy.stats import norm

'''
    S: Current Stock Price
    K: Strike Price
    T: Time to Expiration
    r: Risk-Free Interest Rate
    omege: Volatility
    d1 & d2: Intermediate Steps
    N(.): Cumulative Normal Distribution
'''

def blackScholesCall(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    callPrice = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return callPrice

def blackScholesPut(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    putPrice = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return putPrice

'''
    Comparisons: Model Price vs. Market Price 

    Market Price < Model Price ==> Option is undervalued ==> Consider Buying
    Market Price > Model Price ==> Option is overvalued ==> Avoid Buying
    
'''

