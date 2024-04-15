import json
import random
import string

def generate_dummy_data(num_records):
    dummy_data = []
    for _ in range(num_records):
        record = {
            "id": ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)),
            "name": ''.join(random.choices(string.ascii_letters, k=10)),
            "for_salve": random.choice([True, False]),
            "lat": random.uniform(36.838269, 42.280469),
            "lng": random.uniform(-9.526571, -6.389088),  
            "price": round(random.uniform(0, 1000000), 2)
            
        }
        dummy_data.append(record)
    return dummy_data

if __name__ == "__main__":
    num_records = 60000
    dummy_data = generate_dummy_data(num_records)
    with open("dummy_data.json", "w") as outfile:
        json.dump(dummy_data, outfile, indent=4)
    print("Dummy data generated and saved to dummy_data.json")
