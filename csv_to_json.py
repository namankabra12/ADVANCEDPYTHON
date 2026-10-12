import csv
import json
 
 
def read_csv(path):
    with open(path, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)
 
 
def write_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
 
 
def convert_csv_to_json(csv_path, json_path):
    data = read_csv(csv_path)
    write_json(json_path, data)
    return len(data)
 
 
if __name__ == "__main__":
    csv_path = "students.csv"
    json_path = "students.json"
 
    print("CSV file content:")
    with open(csv_path, "r") as f:
        print(f.read())
 
    count = convert_csv_to_json(csv_path, json_path)
    print("Rows converted:", count)
 
    print()
    print("JSON file content:")
    with open(json_path, "r") as f:
        print(f.read())