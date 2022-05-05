from dtaidistance import dtw_ndim
import numpy
import pandas
import pyarrow.parquet as parquet

table = parquet.read_table('C:\\Users\\ishaa\\source\\repos\\sce_dist\\test\\0000b329-f890-4c2b-93f2-7e2413d4ca5b\\scenario_0000b329-f890-4c2b-93f2-7e2413d4ca5b.parquet', 
    columns=['track_id', 'focal_track_id', 'num_timestamps', 'timestep', 'position_x', 'position_y', 'scenario_id'])

numpy_table = table.to_pandas().to_numpy()

list, main_list = [], []
for i in numpy_table:
    if i[1]==i[0]:
        list.append(numpy.array([i[3], i[4], i[5]]))

print(list)