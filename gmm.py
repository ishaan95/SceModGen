import numpy
import pandas
import pyarrow.parquet as parquet
from matplotlib import pyplot as plt


def find_focal_track():
    #Take one scenario file and try things out
    table = parquet.read_table('C:\\Users\\ishaa\\source\\repos\\sce_dist\\test\\0000b329-f890-4c2b-93f2-7e2413d4ca5b\\scenario_0000b329-f890-4c2b-93f2-7e2413d4ca5b.parquet', 
    columns=['track_id', 'focal_track_id', 'num_timestamps', 'timestep', 'position_x', 'position_y', 'scenario_id'])

    numpy_table = table.to_pandas().to_numpy()
    list, main_list = [], []
    #Isolate focal track. 
    for i in range(numpy.size(numpy_table)):
        list.append(numpy.array([numpy_table[i][0], numpy_table[i][3], numpy_table[i][4], numpy_table[i][5]]))
        if ((i+1)<2013):
            if (numpy_table[i][0] != numpy_table[i+1][0]):
                main_list.append(list)
                list = []
        
    #Final focal track id numpy array
    final = numpy.array(main_list)
    return final