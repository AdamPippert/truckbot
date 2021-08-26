import json
import time
from datetime import date

# Boundaries of Back40 Mine:
# NW: 45.486150, -87.836100
# NE: 45.486150, -87.814900
# SW: 45.471350, -87.836100
# SE: 45.471360, -87.814900

bound_x_min_mine1 = 45.471350
bound_x_max_mine1 = 45.486150
bound_y_min_mine1 = -87.836100
bound_y_max_mine1 = -87.814900

# Boundaries of LeadZinc Mine:
# NW: 42.827450, -90.422000
# NE: 42.827450, -90.404000
# SW: 42.813450, -90.422000
# SE: 42.813450, -90.404000

bound_x_min_mine2 = 42.813450
bound_x_max_mine2 = 42.827450
bound_y_min_mine2 = -90.836100
bound_y_max_mine2 = -90.814900

# Boundaries of Farber Mine:
# NW: 39.288350, -91.532950
# NE: 39.288350, -91.520700
# SW: 39.279300, -91.532950
# SE: 39.279300, -91.520700

bound_x_min_mine3 = 39.279300
bound_x_max_mine3 = 39.288350
bound_y_min_mine3 = -91.532950
bound_y_max_mine3 = -91.520700

filename = truckqueue.json

# Initial truck locations


for i in range (1,100)
    site = random.choice("Back40", "LeadZinc", "Farber")
    truck = random.choice("HAUL001", "HAUL002", "HAUL003")
    if (site == "Back40")
        lat = random.uniform(bound_x_min_mine1, bound_x_max_mine1) 
        lon = random.uniform(bound_y_min_mine1, bound_y_max_mine1)
    if (site == "LeadZinc")
        lat = random.uniform(bound_x_min_mine2, bound_x_max_mine2) 
        lon = random.uniform(bound_y_min_mine2, bound_y_max_mine2)
    if (site == "Farber")
        lat = random.uniform(bound_x_min_mine3, bound_x_max_mine3) 
        lon = random.uniform(bound_y_min_mine3, bound_y_max_mine3)
    speed = 8
    fuel_level = 100
    batt_level = 100
    oil_level = 100
    data[i] = {
        "site": site,
        "truck": truck,
        "lat": lat,
        "lon": lon,
        "speed": speed,
        "fuel_level": fuel_level,
        "batt_level": batt_level,
        "oil_level": oil_level,
        "time": datetime.now.strftime(%Y-%M-%D %H:%M:%S)
    time.sleep(15) # Spacing out truck feeds every 15 seconds 
        
with open(filename, 'w') as f:
    f.write(json.dumps(data, f, indent=4))
