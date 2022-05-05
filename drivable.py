from turtle import color
import gmm
import numpy as np
import pandas
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import patches
import json
from shapely.geometry import polygon, Polygon, Point, LinearRing, LineString

json_file = "C:/Users/ishaa/source/repos/sce_dist/test/0000b329-f890-4c2b-93f2-7e2413d4ca5b"
with open(json_file+"/log_map_archive_0000b329-f890-4c2b-93f2-7e2413d4ca5b.json", "r") as read_file:
    data = json.load(read_file)

x_list_left, x_list_right, y_list_left, y_list_right = [], [], [], []
intersection_trajectories = []
#focal = gmm.find_focal_track()
#print(focal)
plt.figure()
for i in data["lane_segments"]:
    if data["lane_segments"][i]["is_intersection"] is True:
        for j in data["lane_segments"][i]["left_lane_boundary"]:
            x_list_left.append(j['x'])
            y_list_left.append(j['y'])
        for j in data["lane_segments"][i]["right_lane_boundary"]:
            x_list_right.append(j['x'])
            y_list_right.append(j['y'])
        # For drawing intersection polygon only consider first and last elements
        new_list_x = [x_list_left[0], x_list_right[0], x_list_right[-1], x_list_left[-1]]
        new_list_y = [y_list_left[0], y_list_right[0], y_list_right[-1], y_list_left[-1]]
        
        plt.scatter(x_list_left, y_list_left)
        plt.scatter(x_list_right, y_list_right)
        plt.plot()
        plt.show()
        #p = LinearRing([(new_list_x[0],new_list_y[0]), (new_list_x[1],new_list_y[1]),
        #(new_list_x[2],new_list_y[2]), (new_list_x[3],new_list_y[3])])
        #or_p = polygon.orient(p)

        #Check which points of the focal trajectory are inside the current polygon
        temp_list = []
        '''
        for k in focal:
            point_form = Point(k)
            print(point_form)
            if (p.contains(point_form)):
                temp_list.append(point_form)
        intersection_trajectories.append(temp_list)
        '''

#print(intersection_trajectories)







