import csv

def clean_csv(input_file, output_file):
    seen = set()
    cleaned_rows = []

    with open(input_file, 'r', newline='') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            email = row['Email'].strip().lower()
            if email not in seen:
                seen.add(email)
                row['Phone'] = ''.join(filter(str.isdigit, row['Phone']))
                cleaned_rows.append(row)

    with open(output_file, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=cleaned_rows[0].keys())
        writer.writeheader()
        writer.writerows(cleaned_rows)

if __name__ == "__main__":
    print("=== CSV Data Cleaner ===")
    clean_csv('sample_customers.csv', 'cleaned_customers.csv')
    print("Cleaned data saved to cleaned_customers.csv")
