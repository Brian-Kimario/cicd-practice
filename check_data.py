import csv
import sys

def check_ages():
    with open("data.csv") as f:
        reader = csv.DictReader(f)
        errors = []
        for row in reader:
            age = int(row["age"])
            if age < 0:
                errors.append(f"{row['name']} has a negative age: {age}")
    return errors

if __name__ == "__main__":
    problems = check_ages()
    if problems:
        for p in problems:
            print("DATA ERROR:", p)
        sys.exit(1)  # Exits with an error code to fail the CI step
    else:
        print("Data check passed.")
