# Define GARCH parameters
params = {
    'BBRI': {'alpha': 0.0874, 'beta': 0.8835, 'omega': 0.1136},
    'BBCA': {'alpha': 0.1568, 'beta': 0.8432, 'omega': 0.3187},
    'BMRI': {'alpha': 0.1803, 'beta': 0.8197, 'omega': 0.2015},
    'ASII': {'alpha': 0.0680, 'beta': 0.8986, 'omega': 0.1395},
    'TLKM': {'alpha': 0.1379, 'beta': 0.7646, 'omega': 0.3405},
    'PWON': {'alpha': 0.0570, 'beta': 0.9344, 'omega': 0.0511},
    'ICBP': {'alpha': 0.2715, 'beta': 0.4166, 'omega': 0.9593},
    'INDF': {'alpha': 0.1617, 'beta': 0.7397, 'omega': 0.2657},
    'MYOR': {'alpha': 0.1525, 'beta': 0.7573, 'omega': 0.3990},
    'EDGE': {'alpha': 0.4683, 'beta': 0.5317, 'omega': 1.5632},

}

# Adjust parameters if necessary
for stock, param in params.items():
    if param['alpha'] + param['beta'] >= 1:
        param['beta'] = 0.999 - param['alpha']  # Ensure the sum is slightly less than 1

# Function to calculate daily and annual volatility
def calculate_volatility(alpha, beta, omega):
    # Steady-state variance of GARCH(1,1)
    var_daily = omega / (1 - alpha - beta)
    std_daily = np.sqrt(var_daily)
    # Annualize the volatility
    std_annual = std_daily * np.sqrt(252)
    return std_daily, std_annual

# Calculate and print volatilities
volatility_results = {}
for stock, param in params.items():
    std_daily, std_annual = calculate_volatility(param['alpha'], param['beta'], param['omega'])
    volatility_results[stock] = {'Daily Volatility': std_daily, 'Annual Volatility': std_annual}

volatility_results