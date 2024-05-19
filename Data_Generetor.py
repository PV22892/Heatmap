import json
import random
import string

# Define the list of places
places = [
    { "value": "aveiro", "lat_range": (40.5, 40.8), "lng_range": (-8.8, -8.4) },
    { "value": "beja", "lat_range": (37.9, 38.2), "lng_range": (-7.8, -7.5) },
    { "value": "braga", "lat_range": (41.3, 41.6), "lng_range": (-8.7, -8.4) },
    { "value": "braganca", "lat_range": (41.7, 42.0), "lng_range": (-6.9, -6.6) },
    { "value": "castelo_branco", "lat_range": (39.7, 40.0), "lng_range": (-7.4, -7.1) },
    { "value": "coimbra", "lat_range": (40.1, 40.4), "lng_range": (-8.6, -8.3) },
    { "value": "evora", "lat_range": (38.5, 38.8), "lng_range": (-7.8, -7.5) },
    { "value": "faro", "lat_range": (37.0, 37.3), "lng_range": (-8.0, -7.7) },
    { "value": "guarda", "lat_range": (40.5, 40.8), "lng_range": (-7.3, -7.0) },
    { "value": "leiria", "lat_range": (39.7, 40.0), "lng_range": (-8.9, -8.6) },
    { "value": "lisbon", "lat_range": (38.7, 39.0), "lng_range": (-9.3, -9.0) },
    { "value": "portalegre", "lat_range": (39.2, 39.5), "lng_range": (-7.5, -7.2) },
    { "value": "porto", "lat_range": (41.0, 41.3), "lng_range": (-8.8, -8.5) },
    { "value": "santarem", "lat_range": (39.1, 39.4), "lng_range": (-8.8, -8.5) },
    { "value": "setubal", "lat_range": (38.4, 38.7), "lng_range": (-9.0, -8.7) },
    { "value": "viana_do_castelo", "lat_range": (41.5, 41.8), "lng_range": (-8.9, -8.6) },
    { "value": "vila_real", "lat_range": (41.2, 41.5), "lng_range": (-7.8, -7.5) },
    { "value": "viseu", "lat_range": (40.6, 40.9), "lng_range": (-7.9, -7.6) },
    { "value": "azores", "lat_range": (37.5, 38.0), "lng_range": (-28.5, -27.5) },
    { "value": "madeira", "lat_range": (32.5, 33.0), "lng_range": (-17.5, -16.5) }
]

def generate_dummy_data(num_records, places):
    dummy_data = []
    for _ in range(num_records):
        place = random.choice(places)  # Select a random place from the list
        lat_range = place["lat_range"]
        lng_range = place["lng_range"]
        name = place["value"]
        lat = random.uniform(lat_range[0], lat_range[1])
        lng = random.uniform(lng_range[0], lng_range[1])

        record = {
            "id": ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)),
            "name": ''.join(random.choices(string.ascii_letters, k=10)),
            "district": name,
            "for_sale": random.choice([True, False]),
            "lat": lat,
            "lng": lng,
            "price": round(random.uniform(0, 1000000), 2)
        }
        dummy_data.append(record)
    return dummy_data

if __name__ == "__main__":
    num_records = 1000
    dummy_data = generate_dummy_data(num_records, places)
    with open("dummy_data2.json", "w") as outfile:
        json.dump(dummy_data, outfile, indent=4)
    print("Dummy data generated and saved to dummy_data.json")

