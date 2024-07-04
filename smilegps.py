# SMILEgps/smilegps.py

import math


def calculate_wgs84_coordinates(w, h, x, y, lat_center, lon_center, altitude, alpha_width, alpha_height, yaw):
    """
    Calculate new WGS84 coordinates based on image dimensions, camera parameters,
    and position within the image.
    
    Parameters:
    - w, h: Width and height of the image in pixels
    - x, y: Coordinates of the pixel in the image
    - lat_center, lon_center: Latitude and longitude of the center point
    - altitude: Altitude of the camera
    - alpha_width, alpha_height: Field of view angles in width and height directions
    - yaw: Yaw angle of the camera
    
    Returns:
    - new_lat: New latitude based on the calculations
    - new_lon: New longitude based on the calculations
    """

    lat_center = math.radians(lat_center)
    lon_center = math.radians(lon_center)
    alpha_width = math.radians(alpha_width)
    alpha_height = math.radians(alpha_height)
    yaw = math.radians(yaw)

    dx = (x - w / 2) * (2 * altitude * math.tan(alpha_width / 2)) / w
    dy = (h / 2 - y) * (2 * altitude * math.tan(alpha_height / 2)) / h

    distance = math.sqrt(dx**2 + dy**2)

    bearing = math.atan2(dx, dy) + yaw

    delta_lat = distance * math.cos(bearing) / 6371000
    delta_lon = distance * math.sin(bearing) / (6371000 * math.cos(lat_center))

    new_lat = math.degrees(lat_center + delta_lat)
    new_lon = math.degrees(lon_center + delta_lon)

    return new_lat, new_lon
