import csv
import io
import json


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
        escaped_str = san_str.replace('"', r'\"')

        entry = {
            "san_identities": escaped_str,
            "not_before": row["not_before"],
            "not_after": row["not_after"],
            "ca_name": ca_name
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



