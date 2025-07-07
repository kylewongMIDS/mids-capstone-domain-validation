import csv
import io

# def inspect_csv(uploaded_file):
    
#     clean_domain, not_before, not_after = [str], [str], [str]
#     file_text = uploaded_file.read().decode("utf-8").splitlines()[1:]
#     for row in file_text:
#         vals = row.split(',')
#         clean_domain.append(vals[0])
#         not_before.append(vals[1])
#         not_after.append(vals[2])
#     return clean_domain, not_before, not_after

def csv_to_lists(uploaded_file):
    """Convert csv to list"""
    # file_text = uploaded_file.read().decode("utf-8").splitlines()
    # reader = csv.DictReader(file_text)

    # # Extract domain column
    # # clean_domain = [row["clean_domain"] for row in reader if "clean_domain" in row and row["clean_domain"].strip() != ""]
    # # not_before = [row["not_before"] for row in reader if "not_before" in row and row["not_before"].strip() != ""]
    # # not_after = [row["not_after"] for row in reader if "not_after" in row and row["not_after"].strip() != ""]
    
    # clean_domain = [row["clean_domain"] for row in reader]
    # not_before = [row["not_before"] for row in reader]
    # not_after = [row["not_after"] for row in reader]
    
    # return clean_domain, not_before, not_after
    
    clean_domain, not_before, not_after = [], [], []
    file_text = uploaded_file.read().decode("utf-8").splitlines()[1:]
    for row in file_text:
        vals = row.split(',')
        clean_domain.append(vals[0])
        not_before.append(vals[1])
        not_after.append(vals[2])
    return clean_domain, not_before, not_after


def dict_to_csv(data):
    """Convert list of dictionaries to CSV in memory"""
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
    return output.getvalue()
