import random

def random_guess(domains: list[str]) -> list[dict]:
    """returns a random guess for each input"""
    labels = ['good','bad']
    return [{'domain': domain, 'label': random.choice(labels)} for domain in domains]





