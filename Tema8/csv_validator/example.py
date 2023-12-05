# 1. Create a package that reads CSV files and validates their contents based on user-defined rules (e.g., checking for missing values,
# ensuring data types are correct).

from csv_validator.csv_validator import CSValidator

if __name__ == "__main__":
    validator = CSValidator("seeds.csv")
    validator.read_csv()

    validation_rules = [
        {"column": "Perimeter", "validation_type": "missing_values"},
        {"column": "Salary", "validation_type": "data_type", "expected_type": int}
    ]

    errors = validator.validate(validation_rules)

    if errors:
        print("Validation Errors:")
        for error in errors:
            print(error)
    else:
        print("Validation successful.")