import focal_track
from dtaidistance import dtw, dtw_ndim, dtw_visualisation
import numpy

scenario_dir = 'C:\\Users\\ishaa\\source\\repos\\sce_dist\\justTwoScenarios'
tracks = focal_track.getAllFocalTracks(scenario_dir)

track1 = numpy.array(tracks[0])
track2 = numpy.array(tracks[1])

#Re-scaling positions to the 0-1 range for each trajectory
# ranges = numpy.ptp(track1, axis=0)
# scaled_track1, scaled_track2 = [], []
# for i in track1:
#     i[0] = i[0]/ranges[0]
#     i[1] = i[1]/ranges[1]
#     scaled_track1.append(numpy.array([i[0], i[1]]))

# print(scaled_track1)

#distance, paths = dtw_ndim.warping_paths(track1, track2)
#dtw_visualisation.plot_warpingpaths(track1, track2, paths, filename="warp.png")