import math

def calculate_area(x1, y1, x2, y2, x3, y3):
    """
    Oblicza powierzchnię trójkąta na podstawie współrzędnych wierzchołków.
    """
    return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2

def compute_timber_value(x1, y1, x2, y2, x3, y3, GDP, z):
    """
    Oblicza wartość na podstawie powierzchni trójkąta, GDP i parametru z.
    
    Parameters:
    - x1, y1, x2, y2, x3, y3: współrzędne wierzchołków trójkąta
    - GDP: wartość GDP
    - z: parametr
    
    Returns:
    - Wynik obliczeń
    """
    # Obliczanie powierzchni trójkąta
    area = calculate_area(x1, y1, x2, y2, x3, y3)
    
    # Obliczanie wartości na podstawie powierzchni, GDP i parametru z
    result = area * GDP * 40 * (z / 8.5) ** 0.76
    
    return result