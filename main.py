import csv


def read_customers(filename):
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if not rows:
        raise ValueError("The CSV file is empty.")

    headers = rows[0]
    customers = rows[1:]

    if not headers:
        raise ValueError("The CSV file has no column headers.")

    return headers, customers


def check_missing_values(headers, customers):
    missing_counts = {}
    affected_rows = set()

    for header in headers:
        missing_counts[header] = 0

    for row_number, row in enumerate(customers):
        has_missing_value = False

        for column_number, header in enumerate(headers):
            if column_number >= len(row) or row[column_number].strip() == "":
                missing_counts[header] += 1
                has_missing_value = True

        if has_missing_value:
            affected_rows.add(row_number)

    return missing_counts, affected_rows


def check_duplicates(customers):
    seen_rows = set()
    duplicate_count = 0
    affected_rows = set()

    for row_number, row in enumerate(customers):
        row_data = tuple(row)

        if row_data in seen_rows:
            duplicate_count += 1
            affected_rows.add(row_number)
        else:
            seen_rows.add(row_data)

    return duplicate_count, affected_rows


def generate_report(filename):
    try:
        headers, customers = read_customers(filename)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return

    except (ValueError, csv.Error) as error:
        print(f"Error reading CSV file: {error}")
        return

    missing_counts, missing_affected = check_missing_values(
        headers, customers
    )

    duplicate_count, duplicate_affected = check_duplicates(customers)

    all_affected_rows = missing_affected | duplicate_affected

    report = []
    report.append("DATA QUALITY REPORT")
    report.append("=" * 30)
    report.append(f"Total data rows: {len(customers)}")
    report.append("")
    report.append("MISSING VALUES BY COLUMN:")

    for header, count in missing_counts.items():
        report.append(f"{header}: {count}")

    report.append("")
    report.append(f"Duplicate rows: {duplicate_count}")
    report.append(
        f"Rows affected by at least one issue: {len(all_affected_rows)}"
    )

    report_text = "\n".join(report)

    print(report_text)

    try:
        with open("quality_report.txt", "w", encoding="utf-8") as file:
            file.write(report_text)

        print("\nReport saved to quality_report.txt")

    except OSError as error:
        print(f"\nError saving report: {error}")


generate_report("customers.csv")
