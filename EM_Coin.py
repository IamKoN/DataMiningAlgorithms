"""
Nathan Robinson
11/8/2018
Data Mining
Dr. Cho
"""

import numpy as np
import math
from math import factorial

"""Produce the expected values over the flips given the coin's thetas"""
def e_step(flips, theta_A, theta_B):

    heads_coinA, tails_coinA, heads_coinB, tails_coinB = 0, 0, 0, 0
    for flip in flips:
        likelihood_A = probability_coin(flip, theta_A)
        likelihood_B = probability_coin(flip, theta_B)
        prob_A = likelihood_A / (likelihood_A + likelihood_B)
        prob_B = likelihood_B / (likelihood_A + likelihood_B)

        heads_coinA += prob_A * flip.count("H")
        heads_coinB += prob_B * flip.count("H")
        tails_coinA += prob_A * flip.count("T")
        tails_coinB += prob_B * flip.count("T")

    return heads_coinA, tails_coinA, heads_coinB, tails_coinB

"""Produce the values for theta that maximize the expected number of heads or tails"""
def m_step(heads_A, tails_A, heads_B, tails_B):
    theta_A = heads_A / (heads_A + tails_A)
    theta_B = heads_B / (heads_B + tails_B)
    return theta_A, theta_B

"""Return likelihood of initially guesses"""
def probability_coin(flip, probHeads):
    x = flip.count("H")
    n = len(flip)
    return (factorial(n)/(factorial(n-x) * factorial(x))) * pow(probHeads, x) * pow(1 - probHeads, n - x)

"""Iterate through E step and M step"""
def EM_coin(flips, theta_A, theta_B, iters):
    theta_A = theta_A
    theta_B = theta_B
    thetas = [(theta_A, theta_B)]
    iters = iters

    for i in range(iters):
        print("Iteration %d:\t%0.3f %0.3f" % (i, theta_A, theta_B))
        heads_A, tails_A, heads_B, tails_B = e_step(flips, theta_A, theta_B)
        theta_A, theta_B = m_step(heads_A, tails_A, heads_B, tails_B)

    thetas.append((theta_A, theta_B))
    return thetas, (theta_A, theta_B)

flips = [ "HTTTHHTHTH",
          "HHHHTHHHHH",
          "HTHHHHHTHH",
          "HTHTTTHHTT",
          "THHHTHHHTH"]
theta_A = 0.6
theta_B = 0.5
iterations = 11

thetas, _ = EM_coin(flips, theta_A, theta_B, iterations)