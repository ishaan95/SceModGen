import focal_track
from dtaidistance import dtw, dtw_ndim, dtw_visualisation
import numpy
import tensorflow as tf

def getAllFocalTracks():
    scenario_dir = 'C:\\Users\\ishaa\\source\\repos\\sce_dist\\justTwoScenarios'
    tracks = focal_track.getAllFocalTracks(scenario_dir) #All scenarios in the directory
    return tracks

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

# Function below rescales tracks and creates a list of tensors, one tensor 
# for each track
def rescaleTracks(tracks):
    tracks_scaled, track_tensors = [], []
    for track in tracks:
        np_track = numpy.array(track)
        track_scaled = rescaleTrack(np_track)
        np_track_scaled = numpy.array(track_scaled) #One list inside each array
        #tracks_scaled.append(np_track_scaled) #A list of numpy arrays
        track_tensors.append(tf.stack([i for i in tf.data.Dataset.from_tensor_slices(np_track_scaled)]))
    return track_tensors

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