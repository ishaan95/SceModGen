import numpy
import pandas
import pyarrow.parquet as parquet
import glob

def getFocalTrack(scenario_file_path):
    table = parquet.read_table(scenario_file_path, 
    columns=['track_id', 'focal_track_id', 'num_timestamps', 'timestep', 'position_x', 'position_y', 'scenario_id'])

    numpy_table = table.to_pandas().to_numpy()

    list = []
    for i in numpy_table:
        if i[1]==i[0]:
            list.append(numpy.array([i[4], i[5]]))

    return list

def getAllFocalTracks(scenario_directory):
    # A list of scenario file paths
    scenario_file_names = glob.glob(scenario_directory+'\\*\\*.parquet')

    focal_track_list = []
    for i in scenario_file_names:
        focal_track_list.append(getFocalTrack(i))
    return focal_track_list

