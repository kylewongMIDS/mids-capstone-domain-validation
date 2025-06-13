import csv
import io

def csv_to_list(uploaded_file):
    """Convert csv to list"""
    file_text = uploaded_file.read().decode("utf-8").splitlines()
    reader = csv.DictReader(file_text)

    # Extract domain column
    domains = [row["domain"] for row in reader if "domain" in row and row["domain"].strip() != ""]

    return domains


def dict_to_csv(data):
    """Convert list of dictionaries to CSV in memory"""
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
    return output.getvalue()