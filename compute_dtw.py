import focal_track
from dtaidistance import dtw, dtw_ndim, dtw_visualisation
import numpy

scenario_dir = 'C:\\Users\\ishaa\\source\\repos\\sce_dist\\justTwoScenarios'
tracks = focal_track.getAllFocalTracks(scenario_dir)

track1 = numpy.array(tracks[0])
track2 = numpy.array(tracks[1])

# Re-scaling positions to the 0-1 range for each trajectory.
# f(x) = (x-min)/(max-min)
scaled_track1, scaled_track2 = [], []
ranges_track1 = numpy.ptp(track1, axis=0)
minimums_track1 = numpy.amin(track1, axis=0)
for i in track1:
    i[0] = (i[0] - minimums_track1[0])/ranges_track1[0]
    i[1] = (i[1] - minimums_track1[1])/ranges_track1[1]
    scaled_track1.append(numpy.array([i[0], i[1]]))

ranges_track2 = numpy.ptp(track2, axis=0)
minimums_track2 = numpy.amin(track2, axis=0)
for i in track2:
    i[0] = (i[0] - minimums_track2[0])/ranges_track2[0]
    i[1] = (i[1] - minimums_track2[1])/ranges_track2[1]
    scaled_track2.append(numpy.array([i[0], i[1]]))

scaled_track1_inc = numpy.flip(scaled_track1, 0)
scaled_track2_inc = numpy.flip(scaled_track2, 0)

distance, paths = dtw_ndim.warping_paths(scaled_track1_inc, scaled_track2_inc)
dtw_visualisation.plot_warpingpaths(scaled_track2_inc, scaled_track2_inc, paths, filename="warp.png")