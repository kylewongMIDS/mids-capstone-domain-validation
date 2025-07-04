import pandas as pd
# from scipy.stats import entropy
# from collections import Counter
# import Levenshtein
import random
import pickle
from typing import List
# import re


# # Function: check if domain has small edit distance to any whitelist domain
# def has_small_levenshtein(domain, threshold=2):
#     for ref_domain in whitelist_domains:
#         if Levenshtein.distance(domain, ref_domain) <= threshold:
#             return 1
#     return 0


# # Helper functions
# def calc_entropy(domain):
#     prob = [n_x/len(domain) for x,n_x in Counter(domain).items()]
#     return entropy(prob, base=2)


def count_subdomains(domain):
    return len(domain.split('.')) - 2 if '.' in domain else 0


def count_hyphens(domain):
    return domain.count('-')


# def has_unusual_token(domain):
#     tokens = set(re.split(r'[\.\-/_]', domain.lower()))
#     return int(any(token not in safe_tokens for token in tokens))



# Apply
def preprocess_domains(clean_domain_list: List[str], not_before_list: List[str], not_after_list: List[str]) -> pd.DataFrame:
    """"
    Performs feature engineering and selection on submitted domains
    
    Exected input lists:
        - clean_domain (str): the domain
        - not_before (datetime): the start of the certificate's validitiy date
        - not_after (datetime): the end of the certificate's validitiy date
    Returns pd.DataFrame with columns:
        - domain_length (int)
        - shannon_entropy (float)
        - num_subdomains (int)
        - hyphen_count (int)
        - validity_days (int)
        - issued_hour_utc (int)
        - no_domains (int)
        - has_unusual_token (int)
        - small_levenshtein_distance (int)
        - com (int)

    """
    
    df = pd.DataFrame({
        'clean_domain': clean_domain_list,
        'not_before': not_before_list,
        'not_after': not_after_list
    })
    
    # declare input types
    df['not_after'] = pd.to_datetime(df['not_after'])
    df['not_before'] = pd.to_datetime(df['not_before'])
    
    # Feature engineering
    df['domain_length'] = df['clean_domain'].apply(len)
    df['shannon_entropy'] = random.uniform(1,5)
    df['num_subdomains'] = df['clean_domain'].apply(count_subdomains)
    df['hyphen_count'] = df['clean_domain'].apply(count_hyphens)
    df['validity_days'] = (df['not_after'] - df['not_before']).dt.days
    df['issued_hour_utc'] = df['not_before'].dt.hour
    df['no_domains'] = random.randint(0,15) # don't know where this is being calculated
    df['has_unusual_token'] = random.randint(0,1) # don't know where this is being calculated
    df['small_levenshtein_distance'] = random.randint(0,1)
    df['com'] = random.randint(0,15) # don't know where this is being calculated
    
    selected_cols = [
        'domain_length',
        'shannon_entropy',
        'num_subdomains',
        'hyphen_count',
        'validity_days',
        'issued_hour_utc',
        'no_domains',
        'has_unusual_token',
        'small_levenshtein_distance',
        'com'
        ]

    return df[selected_cols]
    

# load the model
def load_model(path=r'src\model\random_forest_model.pkl'):
    with open(path, 'rb') as f:
        model = pickle.load(f)
    return model