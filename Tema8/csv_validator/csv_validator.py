import pandas as pd

class CSValidator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read_csv(self):
        self.data = pd.read_csv(self.file_path)

    def validate(self, rules):
        errors = []
        for rule in rules:
            column_name = rule['column']
            validation_type = rule['validation_type']

            if validation_type == 'missing_values':
                errors.extend(self.check_missing_values(column_name))
            elif validation_type == 'data_type':
                errors.extend(self.check_data_type(column_name, rule['expected_type']))

        return errors

    def check_missing_values(self, column_name):
        missing_values = self.data[column_name].isnull().sum()
        return [f"Column '{column_name}' has {missing_values} missing values."]

    def check_data_type(self, column_name, expected_type):
        incorrect_types = self.data[self.data[column_name].apply(type) != expected_type]
        return [f"Column '{column_name}' has {len(incorrect_types)} values not of type {expected_type}."]

# Example usage
if __name__ == "__main__":
    validator = CSValidator("example.csv")
    validator.read_csv()

    validation_rules = [
        {"column": "Age", "validation_type": "missing_values"},
        {"column": "Salary", "validation_type": "data_type", "expected_type": int}
    ]

    errors = validator.validate(validation_rules)

    if errors:
        print("Validation Errors:")
        for error in errors:
            print(error)
    else:
        print("Validation successful.")