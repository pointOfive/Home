import itertools

def sales_pmf(appt1, appt2, deluxe_sale, std_cost, deluxe_cost):
    pmf_appt_1 = {0:(1-appt1), std_cost:((1-deluxe_sale)*appt1), \
                                    deluxe_cost:(deluxe_sale*appt1)}
    pmf_appt_2 = {0:(1-appt2), std_cost:((1-deluxe_sale)*appt2), \
                                    deluxe_cost:(deluxe_sale*appt2)}


    final_pmf = {}

    for appt_1_outcome, prob1 in pmf_appt_1.iteritems():
        for appt_2_outcome, prob2 in pmf_appt_2.iteritems():
            total_sale = appt_1_outcome + appt_2_outcome
            probability = prob1*prob2
            if total_sale in final_pmf.keys():
                final_pmf[total_sale] += probability
            else:
                final_pmf[total_sale] = probability

    return final_pmf





import numpy as np

def probability_rain(simulation_size=2000):
    '''
    choose the simulation_size

    returns
    -------
    probability that it will rain for at least two days in the next five days,
    knowing that the forecast says that in the next five days the chance of rain
    for each day is 25%
    '''
    total_rainy_days = {k:0 for k in range(6)}
    for sim in xrange(simulation_size):
        rainy_days = 0
        for day in range(5):
            if np.random.random() < 0.25:
                rainy_days += 1
        total_rainy_days[rainy_days] += 1

    print total_rainy_days

    two_or_more = 0
    for count in range(2,6):
        two_or_more += total_rainy_days[count]

    return two_or_more*1. / simulation_size







from scipy.stats import poisson
def is_drug_effective(num_colds, l_drug, l_prior):

    proba = (poisson.pmf(num_colds, l_drug) * 0.75) / \
            (poisson.pmf(num_colds, l_drug) + poisson.pmf(num_colds, l_prior))
    return proba
