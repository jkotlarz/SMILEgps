# SMILEgps/smilegps.py

    import math
    import geopandas as gpd

    def calculate_wgs84_coordinates(w, h, x, y, lat_center, lon_center, altitude, alpha_width, alpha_height, yaw):
        # Konwersja stopni na radiany
        lat_center = math.radians(lat_center)
        lon_center = math.radians(lon_center)
        alpha_width = math.radians(alpha_width)
        alpha_height = math.radians(alpha_height)
        yaw = math.radians(yaw)

        # Oblicz odległości do piksela od środka obrazu
        dx = (x - w / 2) * (2 * altitude * math.tan(alpha_width / 2)) / w
        dy = (h / 2 - y) * (2 * altitude * math.tan(alpha_height / 2)) / h

        # Oblicz odległość do piksela na płaszczyźnie ziemi
        distance = math.sqrt(dx**2 + dy**2)

        # Oblicz kąt azymutu
        bearing = math.atan2(dx, dy) + yaw

        # Oblicz zmianę szerokości i długości geograficznej
        delta_lat = distance * math.cos(bearing) / 6371000
        delta_lon = distance * math.sin(bearing) / (6371000 * math.cos(lat_center))

        # Oblicz nową szerokość i długość geograficzną
        new_lat = math.degrees(lat_center + delta_lat)
        new_lon = math.degrees(lon_center + delta_lon)

        return new_lat, new_lon

# Przykładowe użycie funkcji calculate_wgs84_coordinates
w = 1000  # Szerokość obrazu
h = 800   # Wysokość obrazu
x = 15   # Współrzędna piksela x
y = 16   # Współrzędna piksela y
lat_center = 37.7749  # Szerokość geograficzna środka obrazu
lon_center = -122.4194  # Długość geograficzna środka obrazu
altitude = 1200  # Wysokość nad powierzchnią ziemi
alpha_width = 60  # Szerokość pola widzenia w stopniach
alpha_height = 45  # Wysokość pola widzenia w stopniach
yaw = 120  # Kąt yaw w stopniach

new_lat, new_lon = calculate_wgs84_coordinates(w, h, x, y, lat_center, lon_center, altitude, alpha_width, alpha_height, yaw)

print(f'Nowe współrzędne WGS84: ({new_lat}, {new_lon})')

# Wczytaj plik shapefile
shapefile_path = "shapefile.shp"  # Podaj faktyczną ścieżkę do pliku shapefile
gdf = gpd.read_file(shapefile_path)

# Przejdź przez punkty w pliku shapefile i zastosuj calculate_wgs84_coordinates
for idx, row in gdf.iterrows():
    x = row['x']  # Zakładając, że 'x' to nazwa kolumny z współrzędną x w pliku shapefile
    y = row['y']  # Zakładając, że 'y' to nazwa kolumny z współrzędną y w pliku shapefile

    new_lat, new_lon = calculate_wgs84_coordinates(w, h, x, y, lat_center, lon_center, altitude, alpha_width, alpha_height, yaw)

    print(f'Punkt {idx+1}: Nowe współrzędne WGS84: ({new_lat}, {new_lon})')
