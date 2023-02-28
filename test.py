import math
import geopandas as gpd
from shapely.geometry import Point
import math
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt


# Crear un GeoDataFrame con un rectángulo de 4 lados
rectangle = gpd.GeoDataFrame(geometry=[Polygon([(1, 1), (3, 1), (3, 2), (1, 2)])])
print('Rectángulo original:')
print(rectangle)

# Rotar el rectángulo 45 grados
angle = 45
rad = math.radians(angle)
rotated_rectangle = rectangle.rotate(rad, origin=(2, 1.5))
rotated_rectangle.reset_index(drop=True, inplace=True)
print('Rectángulo rotado:')
print(rotated_rectangle)

