import math

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great-circle distance between two points 
    on the Earth (specified in decimal degrees) using the Haversine formula.
    """
    # Radius of Earth in kilometers
    R = 6371.0
    # R = 3959.0 for miles

    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Differences in coordinates
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance
    distance = R * c
    return distance

# Example usage:
#latA, lonA = 40.7128, -74.0060 # New York City
#latB, lonB = 34.0522, -118.2437 # Los Angeles

#distance_km = haversine_distance(latA, lonA, latB, lonB)
#print(f"Distance: {distance_km:.2f} km") 

