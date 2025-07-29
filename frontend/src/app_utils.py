import csv
import io
import json
import pandas as pd


def csv_to_lists(uploaded_file, ca_name) -> list:
    """
    Converts a CSV file to a list of JSON-like dictionaries in the expected API format.

    Expects columns:
    - san_identities (comma-separated domain strings)
    - not_before (ISO 8601 datetime)
    - not_after (ISO 8601 datetime)
    """
   
    decoded = uploaded_file.read().decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(decoded))
        
    result = []
    for row in reader:
        
        identities = [domain.strip() for domain in row["san_identities"].split(",")]
        san_str = json.dumps(identities)
        
        domain_created = [create_date.strip() for create_date in row["domain_created"].split(",")]
        domain_created_str = json.dumps(domain_created)
        # escaped_str = san_str.replace('"', r'\"')

        entry = {
            "san_identities": san_str,
            "not_before": row["not_before"],
            "not_after": row["not_after"],
            "ca_name": ca_name,
            "domain_created": domain_created_str
        }
        result.append(entry)

    return result




def pred_to_csv(response: dict) -> io.BytesIO:
    
    
    # create text stream
    output = io.StringIO()
    # create csv writer from dictionary input, writes to text stream with column names given
    writer = csv.DictWriter(output, fieldnames=['parsed_domainname', 'prediction'])
    # write the given fieldnames as headers
    writer.writeheader()
    # write each row using given fieldnames within features key
    writer.writerows(response['features'])
    

    # used chatgpt for help on this part
    # streamlit expects binary
    buffer = io.BytesIO()
    buffer.write(output.getvalue().encode("utf-8"))
    buffer.seek(0)
    return buffer


def pred_to_df(response: dict) -> pd.DataFrame:
    """
    Converts prediction response into a pandas DataFrame.

    Parameters:
        response (dict): Dictionary with a 'features' key containing list of dicts.

    Returns:
        pd.DataFrame: DataFrame with parsed_domainname and prediction columns.
    """
    df = pd.DataFrame(response['features'])
    df['risk'] = pd.cut(
                        df['prediction'],
                        bins=[-float('inf'), 0.5, 0.8, 1.0],
                        labels=['low', 'medium', 'high'],
                        right=False
                    )
    return df


def df_to_download_buffer(df: pd.DataFrame) -> io.BytesIO:
    """
    Converts a pandas DataFrame to a CSV and returns a binary buffer for download.

    Parameters:
        df (pd.DataFrame): The DataFrame to convert.

    Returns:
        io.BytesIO: A binary buffer ready for Streamlit download.
    """
    output = io.StringIO()
    df.to_csv(output, index=False)
    
    buffer = io.BytesIO()
    buffer.write(output.getvalue().encode("utf-8"))
    buffer.seek(0)
    return buffer