import csv

def csv_to_list(uploaded_file):
    '''converts uploaded csv to a list'''
    file_text = uploaded_file.read().decode("utf-8").splitlines()
    reader = csv.DictReader(file_text)

    # Extract domain column
    domains = [row["domain"] for row in reader if "domain" in row and row["domain"].strip() != ""]

    return domains