#!/usr/bin/env python3
bike_colors = ['blue', 'blue', 'red', 'blue', 'red', 'red', 'blue', 'blue']
bike_set = set(bike_colors)
for key in bike_set:
    print(bike_colors.count(key), key)


