import focal_track
from dtaidistance import dtw, dtw_ndim, dtw_visualisation
import numpy

scenario_dir = 'C:\\Users\\ishaa\\source\\repos\\sce_dist\\justTwoScenarios'
tracks = focal_track.getAllFocalTracks(scenario_dir)

scenario_dir = 'C:\\Users\\ishaa\\source\\repos\\sce_dist\\justTwoScenarios'
tracks = focal_track.getAllFocalTracks(scenario_dir) #All scenarios in the directory

# Rescaling and reordering between [0-1] and increasing 
def rescaleTrack(track):
    scaled_track = []
    ranges_track = numpy.ptp(track, axis=0)
    minimums_track = numpy.amin(track, axis=0)
    for i in track:
        i[0] = (i[0] - minimums_track[0])/ranges_track[0] # current_x = (current_x-x_min)/(x_max-x_min)
        i[1] = (i[1] - minimums_track[1])/ranges_track[1]
        scaled_track.append(numpy.array([i[0], i[1]]))
    return scaled_track


def rescaleTracks(tracks):
    np_tracks_scaled = []
    for track in tracks:
        np_track = numpy.array(track)
        np_track_scaled = rescaleTrack(np_track)
        np_tracks_scaled.append(np_track_scaled)
    return np_tracks_scaled

'''
# Create a vector containing distance measures between the first track and 
# each other vector. Then repeat for each other track.
def distanceVector(scaled_np_tracks):
    distance_vector_track = []
    for i in range(len(scaled_np_tracks)):
        #d = dtw_ndim.distance(scaled_np_tracks[0], scaled_np_tracks[i])
        #distance_vector_track.append(d)
        distance, paths = dtw_ndim.warping_paths(scaled_np_tracks[0], scaled_np_tracks[i])
        dtw_visualisation.plot_warpingpaths(scaled_np_tracks[0], scaled_np_tracks[i], paths, filename="warp"+str(i)+".png")
        #distance_vector_track.append(tuple(distance, paths))
    return distance_vector_track
'''