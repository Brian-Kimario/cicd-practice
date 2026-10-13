import csv
import sys

def check_ages_and_names():
    with open("data.csv") as f:
        reader = csv.DictReader(f)
        errors = []
        for row in reader:
            # 1. Check for negative age
            age = int(row["age"])
            if age < 0:
                errors.append(f"{row['name']} has a negative age: {age}")
            
            # 2. Check for empty or whitespace-only names
            name = row["name"].strip()
            if not name:
                errors.append("Found a record with a missing or empty name")
                
    return errors

if __name__ == "__main__":
    problems = check_ages_and_names()
    if problems:
        for p in problems:
            print("DATA ERROR:", p)
        sys.exit(1)
    else:
        print("Data check passed.")
