from nada_dsl import *
import random

def nada_main():

    # Define parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")

    # Define secret inputs for each party
    secret_score1 = SecretInteger(Input(name="secret_score1", party=party1)) # Individual's secret score
    secret_score2 = SecretInteger(Input(name="secret_score2", party=party2)) # Trusted 3rd-party's secret score
    secret_score3 = SecretInteger(Input(name="secret_score3", party=party3)) # Another trusted party's secret score

    # Generate random weights for obfuscation
    random_weight1 = Integer(random.randint(1, 100))
    random_weight2 = Integer(random.randint(1, 100))
    random_weight3 = Integer(random.randint(1, 100))

    # Compute the weighted sum of the scores
    weighted_sum = (secret_score1 * random_weight1) + \
                   (secret_score2 * random_weight2) + \
                   (secret_score3 * random_weight3)

    # Compute the total weight
    total_weight = random_weight1 + random_weight2 + random_weight3

    # Compute the weighted average
    weighted_average = weighted_sum / total_weight

    # Define outputs for each party
    output1 = Output(weighted_average, "weighted_average", party1)
    output2 = Output(weighted_average, "weighted_average", party2)
    output3 = Output(weighted_average, "weighted_average", party3)

    return [output1, output2, output3]