import numpy as np
import robin_stocks.robinhood as r
from robin_stocks.robinhood import options

def hestonCall(S0, K, T, r, v0, kappa, theta, sigma, rho, N, M):
    
    dt = T/N
    S = np.full(M, S0)
    v = np.full(M, v0)
    
    for i in range(N):
        Z1 = np.random.normal(size=M)
        Z2 = np.random.normal(size=M)
        
        W1 = Z1
        W2 = rho * Z1 + np.sqrt(1 - rho**2) * Z2
        
        v = np.maximum(v + kappa * (theta - v) * dt + sigma * np.sqrt(v) * np.sqrt(dt) * W2, 0)
        S = S * np.exp((r - 0.5 * v) * dt + np.sqrt(v) * np.sqrt(dt) * W1)
    
    payoff = np.maximum(S - K, 0)
    call_price = np.exp(-r * T) * np.mean(payoff)
    return call_price

