"""
Nathan Robinson
11/8/2018
Data Mining
Dr. Cho
"""

import numpy as np
import math

"""Produce the expected value for sunny_A, cloudy_A, sunny_B, cloudy_B over the temps given the day biases"""
def e_step(temps, mu_Sunny, mu_Cloudy, sd):

    mu_Sunny = mu_Sunny
    mu_Cloudy = mu_Cloudy
    sd = sd
    temps = temps
    e_Sunny, e_Cloudy, sum_eSunnyX, sum_eCloudyX, sum_eSunny, sum_eCloudy = 0, 0, 0, 0, 0, 0
    #e_Sunnys = [e_Sunny]
    #e_Cloudys = [e_Cloudy]

    for temp in temps:
        p_Sunny = probabilty_day(temp,mu_Sunny, sd)
        p_Cloudy = probabilty_day(temp,mu_Cloudy, sd)
        e_Sunny = p_Sunny / (p_Sunny + p_Cloudy)
        e_Cloudy = p_Cloudy / (p_Sunny + p_Cloudy)
        print("prob sunny: \t%0.3f\tprob cloudy:\t%0.3f" % (e_Sunny, e_Cloudy))

        # for M Step
        sum_eSunnyX += e_Sunny * temp
        sum_eCloudyX += e_Cloudy * temp
        sum_eSunny += e_Sunny
        sum_eCloudy += e_Cloudy

        #e_Sunnys.append(e_Sunny)
        #e_Cloudys.append(e_Cloudy)

    #return e_Sunnys, e_Cloudys
    return sum_eSunnyX, sum_eCloudyX, sum_eSunny, sum_eCloudy

"""
def m_step2(temps, e_Sunnys, e_Cloudys):

    e_Sunnys = e_Sunnys
    e_Cloudys = e_Cloudys
    temps = temps

    #e_Sunny, e_Cloudy =  0, 0
    sum_eSunnyX, sum_eCloudyX, sum_eSunny, sum_eCloudy = 0, 0, 0, 0

    for e_Sunny, e_Cloudy, temp in zip(e_Sunnys, e_Cloudys, temps):
        sum_eSunnyX += e_Sunny * temp
        sum_eCloudyX += e_Cloudy * temp
        sum_eSunny += e_Sunny
        sum_eCloudy += e_Cloudy

    mu_Sunny = sum_eSunnyX / sum_eSunny
    mu_Cloudy = sum_eCloudyX / sum_eCloudy

    print("mu sunny:", mu_Sunny, "\nmu cloudy:", mu_Cloudy)

    return mu_Sunny, mu_Cloudy
"""

"""Produce the values for theta that maximize the expected number of sunny/cloudy days"""
def m_step(sum_eSunnyX, sum_eCloudyX, sum_eSunny, sum_eCloudy):

    # Replace dummy values with new implementation
    sum_eSX = sum_eSunnyX
    sum_eCX = sum_eCloudyX
    sum_eS = sum_eSunny
    sum_eC = sum_eCloudy

    mu_Sunny = sum_eSX / sum_eS
    mu_Cloudy = sum_eCX / sum_eC

    print("\nmu sunny: \t%0.3f\tmu cloudy:\t%0.3f" % (mu_Sunny, mu_Cloudy))
    return mu_Sunny, mu_Cloudy

"""Return probabilty of initially chosen average temperatures"""
def probabilty_day(temp, mu, sd):
    x = temp
    mu = mu
    sd = sd
    return pow(math.e, (-(x - mu) ** 2 / (2 * sd ** 2)))

"""Iterate through E step and M step"""
def EM_temp(temps, mu_Sunny, mu_Cloudy, sd, iters):
    temps = temps
    mu_Sunny = mu_Sunny
    mu_Cloudy = mu_Cloudy
    sd = sd
    iters = iters
    mus = [(mu_Sunny, mu_Cloudy)]

    for i in range(iters):
        print("\nIteration %d:\t%0.2f %0.2f" % (i, mu_Sunny, mu_Cloudy))
        sum_eSunnyX, sum_eCloudyX, sum_eSunny, sum_eCloudy = e_step(temps, mu_Sunny, mu_Cloudy, sd)
        mu_Sunny, mu_Cloudy = m_step(sum_eSunnyX, sum_eCloudyX, sum_eSunny, sum_eCloudy)
        #e_Sunnys, e_Cloudys = e_step(temps, mu_Sunny, mu_Cloudy, sd)
        #mu_Sunny, mu_Cloudy = m_step2(temps, e_Sunnys, e_Cloudys)

    mus.append((mu_Sunny, mu_Cloudy))
    return mus, (mu_Sunny, mu_Cloudy)

"""Run EM for Sunny or Cloudy days based on average temperatures"""
temps = [70, 62, 89, 54, 97, 75, 82, 56, 32, 78]
mu_Sunny = 80
mu_Cloudy = 55
sd = 10
iterations = 5

mus, _ = EM_temp(temps, mu_Sunny, mu_Cloudy, sd, iterations)
