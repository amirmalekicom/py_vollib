import implied_volatility as bsm

"""
    :param S: underlying asset price
    :type S: float
    :param K: k price
    :type K: float
    :param sigma: annualized standard deviation, or volatility
    :type sigma: float
    :param t: time to expiration in years
    :type t: float
    :param r: risk-free interest rate
    :type r: float
    :param q: annualized continuous dividend rate
    :type q: float 
    :param flag: 'c' or 'p' for call or put.
    :type flag: str
"""

flag = 'c'
S = 1947
K = 3000
t = 112/365
r = 0.2
sigma = 0.57
q = 0

price = bsm.black_scholes_merton(flag, S, K, t, r, sigma, q)
print('price: {}'.format(price))

price = 57
iv = bsm.implied_volatility(price, S, K, t, r, q, flag)
print('iv: {}'.format(iv))

from py_vollib.black_scholes_merton import black_scholes_merton
from py_vollib.helpers.numerical_greeks import delta as ndelta
from py_vollib.helpers.numerical_greeks import vega as nvega
from py_vollib.helpers.numerical_greeks import theta as ntheta
from py_vollib.helpers.numerical_greeks import rho as nrho
from py_vollib.helpers.numerical_greeks import gamma as ngamma
from py_vollib.black_scholes_merton.greeks.analytical import gamma as agamma
from py_vollib.black_scholes_merton.greeks.analytical import delta as adelta
from py_vollib.black_scholes_merton.greeks.analytical import vega as avega
from py_vollib.black_scholes_merton.greeks.analytical import rho as arho
from py_vollib.black_scholes_merton.greeks.analytical import theta as atheta

flag = 'c'
S = 2049
K = 3000
sigma = 0.57
t = 105/365
r = 0.2
q = 0
epsilon = 0.01

f = lambda flag, S, K, t, r, sigma, b: black_scholes_merton(flag, S, K, t, r, sigma, r-b)


v2 = adelta(flag, S, K, t, r, sigma, q)
print('Delta:\ta={}'.format(v2))

v2 = agamma(flag, S, K, t, r, sigma, q)
print('Gamma:\ta={}'.format(v2))

v2 = arho(flag, S, K, t, r, sigma, q)
print('Rho:\ta={}'.format(v2))

v2 = avega(flag, S, K, t, r, sigma, q)
print('Vega:\ta={}'.format(v2))

v2 = atheta(flag, S, K, t, r, sigma, q)
print('Theta:\ta={}'.format(v2))
